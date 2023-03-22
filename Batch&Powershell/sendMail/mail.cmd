REM open powershell
SET PowerShellDir=C:\Windows\System32\WindowsPowerShell\v1.0
CD /D "%PowerShellDir%"
REM select the powershell file /mail.ps1/
Powershell -ExecutionPolicy Bypass -Command "& '%%%\mail.ps1'"
