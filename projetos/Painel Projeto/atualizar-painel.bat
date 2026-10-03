@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
title Atualizar o painel dos projetos hunter
set "PYTHONIOENCODING=utf-8"

echo.
echo  Painel dos projetos de implantação hunter
echo  =========================================
echo.

rem 1. Achar o Python: o lançador py, o python do PATH ou a instalação do usuário
set "PYEXE="
set "PYARG="
py -3 -c "import sys" >nul 2>&1 && (set "PYEXE=py" & set "PYARG=-3")
if not defined PYEXE python -c "import sys" >nul 2>&1 && set "PYEXE=python"
if not defined PYEXE for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python3*") do if exist "%%~fD\python.exe" set "PYEXE=%%~fD\python.exe"
if not defined PYEXE (
  echo  Não achei o Python neste computador.
  echo  Para instalar, abra o PowerShell e rode:
  echo      winget install Python.Python.3.12 --scope user
  echo  Depois feche esta janela e dê dois cliques de novo neste arquivo.
  echo.
  pause
  exit /b 1
)

rem 2. Instalar o que faltar (pandas lê a planilha, openpyxl abre o xlsx, plotly desenha os gráficos)
"%PYEXE%" %PYARG% -c "import pandas, openpyxl, plotly" >nul 2>&1
if errorlevel 1 (
  echo  Instalando o que falta pro painel: pandas, openpyxl e plotly. Leva um minuto na primeira vez...
  "%PYEXE%" %PYARG% -m pip install --user --quiet --disable-pip-version-check --no-warn-script-location pandas openpyxl plotly
  "%PYEXE%" %PYARG% -c "import pandas, openpyxl, plotly" >nul 2>&1
  if errorlevel 1 (
    echo.
    echo  Não consegui instalar as bibliotecas do Python. Confira a internet e tente de novo.
    echo  O painel que já estava na pasta continua como estava.
    echo.
    pause
    exit /b 1
  )
)

rem 3. Gerar o painel com a exportação do CES mais nova da pasta e abrir no navegador
rem    (a página inicial com TMI, estoque de horas, vazão e carteira sai daqui, sem IA)
echo  Lendo a exportação do CES e montando o painel: página inicial (TMI, estoque de horas,
echo  vazão, horas realizadas, carteira) e as seções do menu lateral...
echo.
"%PYEXE%" %PYARG% gerar_painel.py %*
if errorlevel 1 (
  echo.
  echo  Deu erro ao gerar o painel; a mensagem acima diz o quê.
  echo  O painel que já estava na pasta continua como estava.
  echo  Se faltou a planilha, salve a exportação do CES nesta pasta e dê dois cliques de novo.
  echo.
  pause
  exit /b 1
)

echo.
echo  Pronto: o painel abriu no navegador, na página inicial. Os números de cabeça estão acima.
echo  Esta janela fecha sozinha em 20 segundos.
timeout /t 20 >nul
exit /b 0
