----------
CHCP 65001
@echo off
cls

echo ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
echo ║  Script Choice, Label  ║ 
echo ╚════════════════════════╝

choice /c:LHD /m "Escolha [L]istar [H]ora [D]ata:"

if "%ERRORLEVEL%" == "1" goto LISTAR 
if "%ERRORLEVEL%" == "2" goto HORA
if "%ERRORLEVEL%" == "3" goto DATA
exit

:HORA
cls
echo Hora atual:
time /t
pause
goto FIM

:DATA
cls
echo Data atual:
date /t 
pause
goto FIM

:LISTAR
cls
echo Listagem de diretórios
dir c:\users\%username%\Desktop
pause
goto FIM

:FIM
cls
exit
---------