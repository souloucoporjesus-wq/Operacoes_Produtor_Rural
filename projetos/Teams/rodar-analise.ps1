# rodar-analise.ps1 · roda a análise do Teams sem ninguém na frente e abre o painel no navegador.
# Chamado pela tarefa agendada "Analise do Teams 9h" (seg a sex, 9:00), em cada máquina que tiver
# rodado o instalar-agendamento.bat. Ver _contexto/automacoes.md.
#
# O que faz, em ordem:
#  1. puxa o GitHub;
#  2. se a análise de hoje já existe (a outra máquina fez), só abre o painel;
#  3. se a outra máquina está rodando agora, espera ela terminar (até 60 min) e abre;
#  4. senão, marca "estou rodando", chama o Claude sem janela com a skill analise_teams, gera o
#     painel, envia só os arquivos da pasta do Teams e abre o painel.
# Se falhar: deixa recado em _memoria/recados/ e abre uma página curta dizendo o que houve.
# Uso manual: powershell -ExecutionPolicy Bypass -File rodar-analise.ps1 [-Forcar]

param([switch]$Forcar)

$ErrorActionPreference = "Continue"
$pasta    = $PSScriptRoot
$repo     = Split-Path -Parent (Split-Path -Parent $pasta)
$hoje     = Get-Date -Format "yyyy-MM-dd"
$analises = Join-Path $pasta "analises"
$jsonHoje = Join-Path $analises "$hoje.json"
$painel   = Join-Path $pasta "painel.html"
$log      = Join-Path $pasta "rodar-analise.log"
$origem   = "maquina"
$arqOrigem = Join-Path $repo ".origem"
if (Test-Path $arqOrigem) { $origem = ((Get-Content $arqOrigem -TotalCount 1) -replace '[^A-Za-z0-9_-]', '').Trim() }
if (-not $origem) { $origem = $env:COMPUTERNAME.ToLower() }
$trava    = Join-Path $analises "$hoje.rodando-$origem"
$env:GIT_TERMINAL_PROMPT = "0"
$env:GCM_INTERACTIVE = "never"

New-Item -ItemType Directory -Force $analises | Out-Null

function Log($m) {
    $linha = "{0} [{1}] {2}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $origem, $m
    Add-Content -Path $log -Value $linha -Encoding utf8
}
if ((Test-Path $log) -and ((Get-Content $log).Count -gt 400)) {
    Get-Content $log -Tail 250 | Set-Content $log -Encoding utf8
}

function Recado($assunto, $corpo) {
    $dir = Join-Path $repo "_memoria\recados"
    New-Item -ItemType Directory -Force $dir | Out-Null
    $arq = Join-Path $dir "$hoje-analise-teams-$assunto.md"
    if (Test-Path $arq) { return }
    $txt = "de: analise-teams (tarefa agendada da máquina $origem, 9h)`r`nquando: $(Get-Date -Format 'yyyy-MM-dd HH:mm')`r`nprecisa de ação: sim`r`n`r`n$corpo`r`n`r`nLog: projetos/Teams/rodar-analise.log (só nesta máquina)`r`n"
    Set-Content -Path $arq -Value $txt -Encoding utf8
}

function Abrir-Painel {
    if (Test-Path $painel) { Invoke-Item $painel; Log "painel aberto" }
}

function Pagina-Falha($motivo) {
    $arq = Join-Path $pasta "falha.html"
    $m = [System.Net.WebUtility]::HtmlEncode($motivo)
    $html = "<!doctype html><html lang=`"pt-BR`"><head><meta charset=`"utf-8`"><title>Análise do Teams não rodou</title>" +
        "<style>body{font-family:'Segoe UI',system-ui,sans-serif;background:#f4f6f2;color:#171d18;padding:40px 16px;margin:0}" +
        ".c{max-width:640px;margin:0 auto;background:#fff;border:1px solid #dde3dc;border-radius:12px;padding:20px 22px}" +
        "h1{font-size:19px;margin:0 0 10px}p{line-height:1.5}code{background:#eef1ea;padding:0 4px;border-radius:3px}</style></head>" +
        "<body><div class=`"c`"><h1>A análise do Teams de hoje não rodou</h1><p>$m</p>" +
        "<p>O que continua seguro: as análises anteriores estão intactas em <code>projetos/Teams/analises/</code>.</p>" +
        "<p>Próximo passo: resolva o motivo acima e rode de novo com <code>projetos\Teams\rodar-analise.ps1</code>, " +
        "ou abra o Claude e peça <code>/analise_teams</code>.</p></div></body></html>"
    Set-Content -Path $arq -Value $html -Encoding utf8
    Invoke-Item $arq
}

function Achar-Git {
    $c = Get-Command git -ErrorAction SilentlyContinue
    if ($c) { return $c.Source }
    foreach ($p in @("C:\Program Files\Git\cmd\git.exe", "C:\Program Files (x86)\Git\cmd\git.exe")) { if (Test-Path $p) { return $p } }
    $gd = Get-ChildItem "$env:LOCALAPPDATA\GitHubDesktop\app-*\resources\app\git\cmd\git.exe" -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($gd) { return $gd.FullName }
    return $null
}

function Achar-Claude {
    $c = Get-Command claude -ErrorAction SilentlyContinue
    if ($c) { return $c.Source }
    foreach ($p in @("$env:USERPROFILE\.local\bin\claude.exe", "$env:APPDATA\npm\claude.cmd")) { if (Test-Path $p) { return $p } }
    $ext = Get-ChildItem "$env:USERPROFILE\.vscode\extensions\anthropic.claude-code-*\resources\native-binary\claude.exe" -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($ext) { return $ext.FullName }
    return $null
}

function Achar-Node {
    $c = Get-Command node -ErrorAction SilentlyContinue
    if ($c) { return $c.Source }
    foreach ($p in @("C:\Program Files\nodejs\node.exe", "$env:LOCALAPPDATA\Programs\nodejs\node.exe")) { if (Test-Path $p) { return $p } }
    return $null
}

$git = Achar-Git
function G { & $git -C $repo @args 2>&1 }

function Puxar {
    if (-not $git) { return }
    if (Test-Path (Join-Path $repo ".git\rebase-merge")) { Log "pull pulado: rebase pendente no repositório"; return }
    $r = G pull --rebase --autostash origin main
    if ($LASTEXITCODE -ne 0) { Log "pull falhou: $(($r | Out-String).Trim() -replace '\s+', ' ')"; G rebase --abort | Out-Null }
}

function Enviar($mensagem, $caminhos) {
    if (-not $git) { Log "git não encontrado; o auto-sync ou o /syncar sobem depois"; return }
    foreach ($c in $caminhos) {
        if (Test-Path (Join-Path $repo $c)) { G add -- $c | Out-Null }
        else { G rm --cached --ignore-unmatch -q -- $c | Out-Null }
    }
    G diff --cached --quiet | Out-Null
    if ($LASTEXITCODE -eq 0) { return }
    G commit -m $mensagem | Out-Null
    $r = G pull --rebase --autostash origin main
    if ($LASTEXITCODE -ne 0) { Log "pull antes do envio falhou: $(($r | Out-String).Trim() -replace '\s+', ' ')"; G rebase --abort | Out-Null; return }
    $r = G push origin HEAD:main
    if ($LASTEXITCODE -ne 0) { Log "push falhou: $(($r | Out-String).Trim() -replace '\s+', ' ')" } else { Log "enviado: $mensagem" }
}

function Outras-Travas {
    Get-ChildItem $analises -Filter "$hoje.rodando-*" -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -ne (Split-Path $trava -Leaf) } |
        Where-Object {
            # trava velha (mais de 90 min) não vale: a outra máquina provavelmente caiu no meio
            $txt = Get-Content $_.FullName -TotalCount 1 -ErrorAction SilentlyContinue
            $quando = $null
            if ($txt -match '(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})') { $quando = [datetime]::ParseExact($Matches[1], "yyyy-MM-dd HH:mm:ss", $null) }
            ($quando -ne $null) -and (((Get-Date) - $quando).TotalMinutes -lt 90)
        }
}

# ---------------------------------------------------------------------------------------------
Log "início (forçar: $Forcar)"
Puxar

if ((Test-Path $jsonHoje) -and -not $Forcar) {
    Log "a análise de hoje já existe; só abrindo o painel"
    Abrir-Painel
    exit 0
}

# a outra máquina já está rodando? espera ela (até 60 min)
if (-not $Forcar) {
    $outras = @(Outras-Travas)
    if ($outras.Count -gt 0) {
        Log "outra máquina rodando ($($outras[0].Name)); esperando"
        for ($i = 0; $i -lt 30; $i++) {
            Start-Sleep -Seconds 120
            Puxar
            if (Test-Path $jsonHoje) { Log "a outra máquina terminou"; Abrir-Painel; exit 0 }
            if (@(Outras-Travas).Count -eq 0) { break }
        }
        if (Test-Path $jsonHoje) { Abrir-Painel; exit 0 }
        Log "a outra máquina não terminou; rodando aqui"
    }
}

# marca "estou rodando" e confere empate (as duas ligaram juntas: roda a de nome menor)
Set-Content -Path $trava -Value "$origem $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -Encoding utf8
Enviar "teams: análise de $hoje em andamento ($origem)" @("projetos/Teams/analises/$hoje.rodando-$origem")
$rivais = @(Outras-Travas | Where-Object { $_.Name -lt (Split-Path $trava -Leaf) })
if ($rivais.Count -gt 0 -and -not $Forcar) {
    Log "empate com $($rivais[0].Name); deixando a outra rodar"
    Remove-Item $trava -Force -ErrorAction SilentlyContinue
    Enviar "teams: $origem cede a vez" @("projetos/Teams/analises/$hoje.rodando-$origem")
    for ($i = 0; $i -lt 30; $i++) {
        Start-Sleep -Seconds 120
        Puxar
        if (Test-Path $jsonHoje) { Abrir-Painel; exit 0 }
    }
    Log "a outra máquina não entregou em 60 min"
    Pagina-Falha "A outra máquina começou a análise de hoje e não terminou em 60 minutos."
    exit 1
}

$claude = Achar-Claude
if (-not $claude) {
    Log "Claude não encontrado"
    Remove-Item $trava -Force -ErrorAction SilentlyContinue
    Enviar "teams: $origem sem Claude" @("projetos/Teams/analises/$hoje.rodando-$origem")
    Recado "sem-claude" "Não achei o Claude Code nesta máquina ($origem). Instale a extensão do Claude Code no VS Code (ou o Claude Code de linha de comando) e faça login uma vez."
    Pagina-Falha "Não achei o Claude Code nesta máquina. Instale a extensão do Claude Code no VS Code (ou o Claude Code de linha de comando) e faça login uma vez."
    exit 1
}

$ferramentas = @(
    "Read", "Write", "Edit", "Glob", "Grep", "ToolSearch", "Agent", "TodoWrite", "Bash(node:*)",
    "mcp__claude_ai_Microsoft_365__get_me",
    "mcp__claude_ai_Microsoft_365__chat_message_search",
    "mcp__claude_ai_Microsoft_365__read_resource",
    "mcp__claude_ai_Microsoft_365__teams_list_chats",
    "mcp__claude_ai_Microsoft_365__teams_list_teams",
    "mcp__claude_ai_Microsoft_365__teams_list_channels",
    "mcp__claude_ai_Microsoft_365__teams_list_channel_messages"
) -join ","

$pedido = "Rode a skill analise_teams em modo rotina. Hoje e $hoje. A pasta do Teams e projetos/Teams. " +
    "Nao rode granola, briefing, iniciar nem atualizar, e ignore o gatilho de primeiro comando do dia: esta sessao e so a rotina. " +
    "Nunca envie mensagem no Teams. Nao mexa em git nem abra navegador: o script que te chamou faz isso. " +
    "No fim, responda so com: ok $hoje e o numero de pendencias criticas."

Log "chamando o Claude ($claude)"
Push-Location $repo
$saida = & $claude -p $pedido --allowedTools $ferramentas --permission-mode acceptEdits --output-format text 2>&1
$codigo = $LASTEXITCODE
Pop-Location
$resumoSaida = (($saida | Out-String).Trim() -replace '\s+', ' ')
if ($resumoSaida.Length -gt 400) { $resumoSaida = $resumoSaida.Substring(0, 400) + "..." }
Log "Claude terminou (código $codigo): $resumoSaida"

Remove-Item $trava -Force -ErrorAction SilentlyContinue

if (-not (Test-Path $jsonHoje)) {
    Enviar "teams: análise de $hoje falhou ($origem)" @("projetos/Teams/analises/$hoje.rodando-$origem")
    $motivo = "O Claude rodou mas não gravou a análise de hoje. Resposta dele: $resumoSaida"
    if ($resumoSaida -match "auth|autentic|login|OAuth|401|403") {
        $motivo = "O Microsoft 365 (Teams) pediu login de novo. Abra o Claude nesta máquina, rode /mcp e reconecte o Microsoft 365; depois rode de novo. Resposta: $resumoSaida"
    }
    Recado "falhou" $motivo
    Pagina-Falha $motivo
    exit 1
}

# garante o painel gerado (o Claude já deve ter rodado o gerador; rodar de novo não estraga)
$node = Achar-Node
if ($node) {
    $g = & $node (Join-Path $pasta "gerar-painel.js") $hoje 2>&1
    Log "gerador: $(($g | Out-String).Trim() -replace '\s+', ' ')"
}

Enviar "teams: análise $hoje ($origem)" @(
    "projetos/Teams/analises/$hoje.json", "projetos/Teams/analises/$hoje.html", "projetos/Teams/analises/$hoje.md",
    "projetos/Teams/painel.html", "projetos/Teams/analises/$hoje.rodando-$origem"
)
Abrir-Painel
Log "fim"
exit 0
