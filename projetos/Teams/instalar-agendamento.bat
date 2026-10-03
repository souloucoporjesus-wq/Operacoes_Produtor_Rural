@echo off
rem Liga a analise do Teams das 9h nesta maquina. Duplo clique, uma vez em cada computador.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0instalar-agendamento.ps1"
echo.
pause
