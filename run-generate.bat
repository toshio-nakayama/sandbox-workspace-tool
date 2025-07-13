@echo off
REM run-generate.bat

REM スクリプトをこのバッチのある場所から呼び出す
python "%~dp0\generate-workspace.py"

REM 完了後にウィンドウをそのままにする
pause
