# instalar-agendamento.ps1 · liga a análise do Teams das 9h nesta máquina (tarefa agendada do Windows).
# Rodar uma vez em cada máquina (duplo clique no instalar-agendamento.bat). Rodar de novo só atualiza.
# Pra desligar: powershell -ExecutionPolicy Bypass -File instalar-agendamento.ps1 -Remover

param([switch]$Remover, [switch]$Testar)

$nome = "Analise do Teams 9h"
$pasta = $PSScriptRoot
$script = Join-Path $pasta "rodar-analise.ps1"

if ($Remover) {
    Unregister-ScheduledTask -TaskName $nome -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "Tarefa '$nome' removida desta máquina."
    exit 0
}

Write-Host ""
Write-Host "Conferindo o que a análise precisa nesta máquina..."
$ok = $true

$claude = Get-Command claude -ErrorAction SilentlyContinue
if (-not $claude) {
    $claude = Get-ChildItem "$env:USERPROFILE\.vscode\extensions\anthropic.claude-code-*\resources\native-binary\claude.exe" -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending | Select-Object -First 1
}
if (-not $claude) {
    foreach ($p in @("$env:USERPROFILE\.local\bin\claude.exe", "$env:APPDATA\npm\claude.cmd")) { if (Test-Path $p) { $claude = Get-Item $p } }
}
if ($claude) { Write-Host "  [ok] Claude Code encontrado" } else { Write-Host "  [falta] Claude Code: instale a extensão do Claude Code no VS Code e faça login"; $ok = $false }

$node = Get-Command node -ErrorAction SilentlyContinue
if (-not $node -and (Test-Path "C:\Program Files\nodejs\node.exe")) { $node = Get-Item "C:\Program Files\nodejs\node.exe" }
if ($node) { Write-Host "  [ok] Node.js encontrado" } else { Write-Host "  [falta] Node.js: instale em https://nodejs.org (versão LTS)"; $ok = $false }

$git = Get-Command git -ErrorAction SilentlyContinue
if (-not $git -and (Test-Path "C:\Program Files\Git\cmd\git.exe")) { $git = Get-Item "C:\Program Files\Git\cmd\git.exe" }
if (-not $git) { $git = Get-ChildItem "$env:LOCALAPPDATA\GitHubDesktop\app-*\resources\app\git\cmd\git.exe" -ErrorAction SilentlyContinue | Select-Object -First 1 }
if ($git) { Write-Host "  [ok] git encontrado" } else { Write-Host "  [aviso] git não encontrado: a análise roda, mas não sobe pro GitHub sozinha" }

$repo = Split-Path -Parent (Split-Path -Parent $pasta)
if (Test-Path (Join-Path $repo ".origem")) { Write-Host "  [ok] origem desta máquina: $((Get-Content (Join-Path $repo '.origem') -TotalCount 1).Trim())" }
else { Write-Host "  [aviso] sem arquivo .origem na raiz: rode o /setup nesta máquina pra ela ter um nome (usa o nome do computador por enquanto)" }

$acao = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$script`"" -WorkingDirectory $pasta
$gatilho = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday, Tuesday, Wednesday, Thursday, Friday -At "09:00"
$config = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Hours 2) -MultipleInstances IgnoreNew
$quem = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $nome -Action $acao -Trigger $gatilho -Settings $config -Principal $quem -Force `
    -Description "Análise do Teams do Julio (skill analise_teams): lê o Teams, gera o painel em projetos/Teams e abre no navegador. Seg a sex, 9h. Se o computador estiver desligado às 9h, roda quando ligar." | Out-Null

Write-Host ""
Write-Host "Tarefa '$nome' ligada: segunda a sexta às 9:00 (se o computador estiver desligado, roda assim que ligar)."
if (-not $ok) { Write-Host "Falta instalar o que está marcado [falta] acima, senão ela não vai conseguir rodar." }
if ($Testar) {
    Start-ScheduledTask -TaskName $nome
    Write-Host "Rodando agora em segundo plano. O painel abre sozinho no navegador quando terminar (uns 10 a 20 minutos)."
}
