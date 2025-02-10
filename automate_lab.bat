@echo off
echo Launching essential applications...
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe"
start "" "C:\Program Files\Microsoft SQL Server\150\Tools\Binn\ManagementStudio\Ssms.exe"
start "" "C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"

echo Checking MSSQL$SQLEXPRESS service status...
sc query MSSQL$SQLEXPRESS | find "RUNNING" > nul
if %errorlevel% == 0 (
    echo MSSQL$SQLEXPRESS service is already running.
) else (
    echo Starting MSSQL$SQLEXPRESS service...
    net start MSSQL$SQLEXPRESS
    if %errorlevel% == 0 (
        echo MSSQL$SQLEXPRESS started successfully.
    ) else (
        echo Failed to start MSSQL$SQLEXPRESS.
    )
)

echo Opening Python lab files...
cd /d "C:\Users\%USERNAME%\Documents\ML_Labs"
start "" "Lab2.py"
start "" "Lab3py"

echo All tasks executed successfully!
pause
