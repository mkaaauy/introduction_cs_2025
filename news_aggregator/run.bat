@echo off
cd /d "%~dp0"
python -m pip install -r requirements.txt -q
python manage.py migrate --noinput
python manage.py runserver 127.0.0.1:8000
