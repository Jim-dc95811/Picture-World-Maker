@echo off
setlocal
cd /d "%~dp0"
title Picture World Maker v0.2.5
echo Starting Ready to Fly - on an older PC this first step can take a few minutes, please wait...
echo (Windows Defender may check the files first and slow the PC. That is normal - do not close this window.)
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0System Files\Ready_To_Fly.ps1" -Folder "%~dp0System Files" -Tool "Picture World Maker" -Packages "Pillow" -Imports "PIL" -NeedTk
if errorlevel 1 goto rtf_stopped
set "PYEXE="
set /p PYEXE=<"%~dp0System Files\python_path.txt"
if not defined PYEXE goto rtf_stopped
set PYTHONDONTWRITEBYTECODE=1
rem the window program (no black console) sits beside python.exe
set "PYWEXE=%PYEXE:python.exe=pythonw.exe%"
if not exist "%PYWEXE%" set "PYWEXE=%PYEXE%"
start "" "%PYWEXE%" "System Files\START PICTURE WORLD MAKER.pyw"
exit /b 0

:rtf_stopped
echo.
echo Picture World Maker did not start - read the message above.
echo A log is in System Files\Ready_To_Fly_log.txt
pause
exit /b 1
