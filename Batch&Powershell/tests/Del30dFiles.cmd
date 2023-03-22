@echo off

REM delete files from 30d or less in a directory
echo Deleting files
forfiles /p "C:\Users\%%%\" /s /m *.log /D -30 /C "cmd /c del @path"
echo files deleted