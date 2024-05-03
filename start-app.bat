@echo off
IF NOT EXIST .env (
    python -m venv .env
    cd .env\Scripts
    call activate.bat
    cd ../..
    pip install -r requirements.txt
) ELSE (
    cd .env\Scripts
    call activate.bat
    cd ../..
)
cd src
python.exe manage.py runserver