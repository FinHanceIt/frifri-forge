@echo off
REM assemble-plugins.cmd - copies Fri's 18 plugin folders into frifri-forge\plugins\
REM Run this from inside the frifri-forge folder (double-click or: .\assemble-plugins.cmd)
setlocal
set "ROOT=%~dp0"
set "PARENT=%ROOT%.."
echo Assembling plugins into "%ROOT%plugins" ...
echo.

call :cp "AevumForge\aevumforge"                     aevumforge
call :cp "ChronoForge"                               chronoforge
call :cp "CouncilOfTheScythe\council-of-the-scythe"  council-of-the-scythe
call :cp "GuardForge\guardforge"                     guardforge
call :cp "IdeaForge\ideaforge"                       ideaforge
call :cp "InkForge\inkforge"                          inkforge
call :cp "LLMForge\llmforge"                          llmforge
call :cp "OfertaForge\ofertaforge"                   ofertaforge
call :cp "OriginForge\originforge"                   originforge
call :cp "PsycheForge\plugin-src"                    psycheforge
call :cp "SearchForge"                                searchforge
call :cp "ShipForge\shipforge"                        shipforge
call :cp "Statecraft"                                 statecraft
call :cp "TheoForge\theoforge"                        theoforge
call :cp "TrendForge"                                 trendforge
call :cp "WaveForge\waveforge"                        waveforge
call :cp "appfactory-enterprise"                     appfactory-enterprise
call :cp "cairn-harness-plugin"                      cairn-harness

echo.
echo Done. Folders now in plugins\:
dir /b "%ROOT%plugins"
echo.
echo Sanity: each should contain a .claude-plugin\plugin.json
goto :eof

:cp
robocopy "%PARENT%\%~1" "%ROOT%plugins\%~2" /E /XD .git node_modules reports /XF *.plugin .stryker.gate.json >nul
if errorlevel 8 (echo   FAILED: %~2) else (echo   ok: %~2)
exit /b 0
