
@echo off

cls
echo.
echo Start Driver Installation
echo.

powershell.exe -Command "start-process -Wait -Verb 'RunAs' -FilePath 'powershell.exe' -ArgumentList @('-executionpolicy','bypass','-File','%~dp0.\installDriverHelper.ps1')"

echo.
echo Finished.
echo.
echo Reboot after pressing button.
echo.

shutdown /r /t 3