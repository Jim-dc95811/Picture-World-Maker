@echo off
setlocal
cd /d "%~dp0"
py -3.14 -c "import PIL" >nul 2>nul
if errorlevel 1 (
  echo Pillow is not installed yet. Installing it now - one time only...
  py -3.14 -m pip install Pillow
)
py -3.14 "System Files\RPF_SELF_TEST.py"
if errorlevel 1 (
  echo.
  echo SELF TEST FAILED
) else (
  echo.
  echo SELF TEST PASSED
)
pause
endlocal
