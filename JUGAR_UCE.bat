@echo off
title UCE Central Explorer - Servidor
echo ========================================================
echo   INICIANDO CENTRAL EXPLORER: MISTERIO DEL RELOJ DEL SOL
echo ========================================================
echo.
echo Levantando el servidor de la universidad... por favor espera.

:: Abre una nueva ventana que ejecuta tu script de Python
start cmd /k "python app.py"

:: Espera 3 segundos para darle tiempo al servidor de encenderse
timeout /t 3 /nobreak > NUL

:: Abre automáticamente tu navegador predeterminado en el juego
start http://localhost:5000

exit
