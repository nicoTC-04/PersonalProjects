REM .bat file to round date to the friday of the current week
REM used for an assignment in internship

@echo off

set EXPORT_TIMESTAMP_TIME=%TIME:~0,8%
set EXPORT_TIMESTAMP_TIME=%EXPORT_TIMESTAMP_TIME: =0%


set EXPORT_TIMESTAMP_FILE=%DATE:~-4%%DATE:~4,2%%DATE:~7,2%_%EXPORT_TIMESTAMP_TIME:~0,2%%EXPORT_TIMESTAMP_TIME:~3,2%%EXPORT_TIMESTAMP_TIME:~6,2%

echo %EXPORT_TIMESTAMP_FILE%

for /f %%i in ('powershell ^(get-date^).DayOfWeek') do set dow=%%i

echo %dow%



REM Funtions to change date
setlocal


REM Get the current date
REM Will return variables YY, YYYY, MM, DD, HH, Min and Sec
Call :GetDateTime

REM verify current date
if %dow% == Monday goto lunes
if %dow% == Tuesday goto martes
if %dow% == Wednesday goto miercoles
if %dow% == Thursday goto jueves
if %dow% == Friday goto viernes
if %dow% == Saturday goto sabado
if %dow% == Sunday goto domingo

:lunes
Call :AddSubDate %YYYY% %MM% %DD% +4 nuevo
REM echo hoy    : %YYYY%%MM%%DD%
REM echo nuevo   : %nuevo%
goto PrintNuevo

:martes
Call :AddSubDate %YYYY% %MM% %DD% +3 nuevo
REM echo hoy    : %YYYY%%MM%%DD%
REM echo nuevo   : %nuevo%
goto PrintNuevo

:miercoles
Call :AddSubDate %YYYY% %MM% %DD% +2 nuevo
REM echo hoy    : %YYYY%%MM%%DD%
REM echo nuevo   : %nuevo%
goto PrintNuevo

:jueves
Call :AddSubDate %YYYY% %MM% %DD% +1 nuevo
REM echo hoy    : %YYYY%%MM%%DD%
REM echo nuevo   : %nuevo%
goto PrintNuevo

:viernes
Call :AddSubDate %YYYY% %MM% %DD% +0 nuevo
REM echo hoy    : %YYYY%%MM%%DD%
REM echo nuevo   : %nuevo%
goto PrintNuevo

:sabado
Call :AddSubDate %YYYY% %MM% %DD% -1 nuevo
REM echo hoy    : %YYYY%%MM%%DD%
REM echo nuevo   : %nuevo%
goto PrintNuevo

:domingo
Call :AddSubDate %YYYY% %MM% %DD% -2 nuevo
REM echo hoy    : %YYYY%%MM%%DD%
REM echo nuevo   : %nuevo%
goto PrintNuevo

:AddSubDate Year Month Day <+/-Days> RetVar
setlocal & set a=%4
set "yy=%~1"&set "mm=%~2"&set "dd=%~3"
set /a "yy=10000%yy% %%10000,mm=100%mm% %% 100,dd=100%dd% %% 100"
if %yy% LSS 100 set /a yy+=2000 &rem Adds 2000 to two digit years
set /a JD=dd-32075+1461*(yy+4800+(mm-14)/12)/4+367*(mm-2-(mm-14)/12*12)/12-3*((yy+4900+(mm-14)/12)/100)/4
if %a:~0,1% equ + (set /a JD=%JD%+%a:~1%) else set /a JD=%JD%-%a:~1%
set /a L= %JD%+68569,     N= 4*L/146097, L= L-(146097*N+3)/4, I= 4000*(L+1)/1461001
set /a L= L-1461*I/4+31, J= 80*L/2447,  K= L-2447*J/80,      L= J/11
set /a J= J+2-12*L,      I= 100*(N-49)+I+L
set /a YYYY= I, MM=100+J, DD=100+K
set MM=%MM:~-2% & set DD=%DD:~-2%
set ret=%YYYY: =%%MM: =%%DD: =%
endlocal & set %~5=%ret%
exit /b

:GetDateTime Year Month Day Hour Minute Second
@echo off & setlocal
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
( ENDLOCAL
   set "YY=%YY%" 
   set "YYYY=%YYYY%" 
   set "MM=%MM%" 
   set "DD=%DD%"
   set "HH=%HH%" 
   set "Min=%Min%"
   set "Sec=%Sec%"
)
exit /b


:PrintNuevo
REM Print new date
set NEW_TIMESTAMP=%nuevo%_%EXPORT_TIMESTAMP_TIME:~0,2%%EXPORT_TIMESTAMP_TIME:~3,2%%EXPORT_TIMESTAMP_TIME:~6,2%
echo %NEW_TIMESTAMP%
exit /b