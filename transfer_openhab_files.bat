@echo off

REM Lokale Ordner
set "sourceItems=C:\Projekte\xml2OH\export\items"
set "sourceThings=C:\Projekte\xml2OH\export\things"

REM Zielordner auf dem OpenHAB-Server
set "targetItems=\\galactus\openHAB-conf\items"
set "targetThings=\\galactus\openHAB-conf\things"

REM Benutzername und Passwort (falls nötig)
set "username=openhab"
set "password=openhab"

REM Verbindung zur SMB-Freigabe herstellen (falls notwendig)
REM Falls keine Anmeldung nötig ist, diese Zeilen auskommentieren oder löschen.
net use %targetItems% /user:%username% %password% >nul 2>&1
net use %targetThings% /user:%username% %password% >nul 2>&1

REM Dateien aus dem "items"-Ordner kopieren
echo Kopiere Dateien aus "%sourceItems%" nach "%targetItems%"...
xcopy "%sourceItems%\*" "%targetItems%\" /E /Y /Q
if %ERRORLEVEL% equ 0 (
    echo Items-Dateien erfolgreich kopiert!
) else (
    echo FEHLER: Beim Kopieren der Items-Dateien ist ein Fehler aufgetreten!
)

REM Dateien aus dem "things"-Ordner kopieren
echo Kopiere Dateien aus "%sourceThings%" nach "%targetThings%"...
xcopy "%sourceThings%\*" "%targetThings%\" /E /Y /Q
if %ERRORLEVEL% equ 0 (
    echo Things-Dateien erfolgreich kopiert!
) else (
    echo FEHLER: Beim Kopieren der Things-Dateien ist ein Fehler aufgetreten!
)

REM Verbindung zur SMB-Freigabe trennen (falls hergestellt)
net use %targetItems% /delete >nul 2>&1
net use %targetThings% /delete >nul 2>&1

echo Übertragung abgeschlossen!
pause