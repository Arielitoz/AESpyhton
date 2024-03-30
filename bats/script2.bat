----------
CHCP 65001
@echo off
cls

echo ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
echo ║   Script - Logs        ║ 
echo ╚════════════════════════╝

cd c:\users\%username%\Desktop

set /a num=%random% %%100+1

echo --- INICIO DA EXECUCAO DO SCRIPT ---
echo [ _________________________________]
echo Numero sorteado: %num%

if %num% gtr 50 (
echo %num% >> arquivo.txt
) else (
goto naoexiste
)

if exist arquivo.txt (
goto existe
) else (
goto naoexiste
)

:existe 
echo %username%;%date%;%time%;S >> log.txt
echo ARQUIVO ENCONTRADO/ EXISTE
type log.txt
goto remocao
pause

:naoexiste
echo %USERNAME%;%DATE%;%TIME%;N >> log.txt
echo ARQUIVO NAO ENCONTRADO / NAO EXISTE
type log.txt
goto remocao
pause

:remocao
if exist arquivo.txt (
del arquivo.txt 
)

echo [ _________________________________]
echo --- FIM DA EXECUCAO DO SCRIPT ---


echo Obrigado
pause
exit