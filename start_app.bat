@echo off
title Person Re-ID Application Launcher
cd /d "%~dp0"

echo.
echo ============================================================
echo    Person Re-Identification System
echo ============================================================
echo.

echo [1/2] Starting Backend Server...
start "Backend Server" cmd /k "cd backend && python app.py"
timeout /t 2 /nobreak >nul
echo       [OK] Backend starting on http://localhost:5000

echo.
echo [2/2] Starting Frontend...
cd frontend
start "Frontend Server" cmd /k "npm start"

echo.
echo ============================================================
echo   Application Starting...
echo.
echo   Frontend: http://localhost:3000
echo   Backend:  http://localhost:5000
echo.
echo   Both servers will open in new windows.
echo   Press any key to close this window...
echo ============================================================
pause >nul
