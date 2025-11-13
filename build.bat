@echo off
title 🔧 Build Auto Clicker

echo Mengecek dan menginstal dependensi...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Membangun file .exe...
pyinstaller --onefile --noconsole autoclicker.py

echo.
echo ✅ Selesai! Cek folder dist\autoclicker.exe
pause
