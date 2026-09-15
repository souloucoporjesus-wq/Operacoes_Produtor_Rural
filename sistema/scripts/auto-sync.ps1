# auto-sync.ps1 · sincroniza esta pasta com o GitHub sem ninguém na frente.
# Roda pela tarefa agendada "RatosOS auto-sync" a cada 30 minutos (ver _contexto/automacoes.md).
# O que faz: puxa o que mudou no GitHub, commita o que mudou aqui, envia. Só isso.
# Se der conflito, aborta sem mexer em nada e deixa um recado em _memoria/recados/.
# Log local em sistema/scripts/auto-sync.log (não sobe pro git: .log é bloqueado no .gitignore).

$ErrorActionPreference = "Continue"
$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$git  = "C:\Program Files\Git\cmd\git.exe"
$log  = Join-Path $PSScriptRoot "auto-sync.log"
$env:GIT_TERMINAL_PROMPT = "0"
$env:GCM_INTERACTIVE = "never"

function Log($msg) {
    $line = "{0} {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $msg
    Add-Content -Path $log -Value $line -Encoding utf8
}

function Recado($assunto, $corpo) {
    $dir = Join-Path $repo "_memoria\recados"
    New-Item -ItemType Directory -Force $dir | Out-Null
    $hoje = Get-Date -Format "yyyy-MM-dd"
    $arq = Join-Path $dir "$hoje-auto-sync-$assunto.md"
    if (Test-Path $arq) { return }  # um recado por assunto por dia basta
    $txt = @"
de: auto-sync (tarefa agendada desta máquina)
quando: $(Get-Date -Format "yyyy-MM-dd HH:mm")
precisa de ação: sim

$corpo

Log completo: sistema/scripts/auto-sync.log
"@
    Set-Content -Path $arq -Value $txt -Encoding utf8
}

# mantém o log enxuto (últimas 500 linhas)
if ((Test-Path $log) -and ((Get-Content $log).Count -gt 500)) {
    Get-Content $log -Tail 300 | Set-Content $log -Encoding utf8
}

Set-Location $repo

# se um rebase anterior ficou pela metade, não toca em nada
if (Test-Path (Join-Path $repo ".git\rebase-merge")) {
    Log "PULADO: rebase pendente no repositório, resolve na mão"
    exit 0
}

# 1. puxa o que mudou lá
$pull = & $git pull --rebase --autostash origin main 2>&1
if ($LASTEXITCODE -ne 0) {
    Log "PULL FALHOU: $($pull -join ' | ')"
    & $git rebase --abort 2>&1 | Out-Null
    if ($pull -match "CONFLICT|conflict") {
        Recado "conflito" "O pull do GitHub deu conflito e eu abortei sem mexer em nada. Abre o GitHub Desktop (ou roda /syncar) pra resolver. Até lá, nada sobe."
    } elseif ($pull -match "Authentication|could not read Username|403") {
        Recado "login" "O git não conseguiu autenticar no GitHub. Roda um push pelo terminal uma vez (git push) pra refazer o login do credential manager."
    }
    exit 1
}

# 2. commita o que mudou aqui
& $git add -A 2>&1 | Out-Null
$status = & $git status --porcelain
if ($status) {
    $origem = "dono"
    $arqOrigem = Join-Path $repo ".origem"
    if (Test-Path $arqOrigem) { $origem = (Get-Content $arqOrigem -Raw).Trim() }
    $n = ($status | Measure-Object).Count
    $msg = "auto-sync $(Get-Date -Format 'yyyy-MM-dd HH:mm') ($origem): $n arquivo(s)"
    $commit = & $git commit -q -m $msg 2>&1
    if ($LASTEXITCODE -ne 0) { Log "COMMIT FALHOU: $($commit -join ' | ')"; exit 1 }
    Log "commit: $msg"
}

# 3. envia (só se tem algo pra enviar)
$ahead = & $git rev-list --count origin/main..main 2>$null
if ([int]$ahead -gt 0) {
    $push = & $git push origin main 2>&1
    if ($LASTEXITCODE -ne 0) {
        Log "PUSH FALHOU: $($push -join ' | ')"
        if ($push -match "Authentication|could not read Username|403") {
            Recado "login" "O git não conseguiu autenticar no GitHub na hora do push. Roda um push pelo terminal uma vez (git push) pra refazer o login do credential manager."
        }
        exit 1
    }
    Log "push ok ($ahead commit(s))"
} else {
    Log "nada pra enviar"
}
exit 0
