@echo off
setlocal

where python3 > nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3 is not installed. Please download and install Python from:
    echo https://www.python.org/downloads/
    exit /b 1
)

if not exist venv\Scripts\activate.bat (
    python3 -m venv venv
)

call venv\Scripts\activate.bat

python3 -m pip install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate

start cmd /k python3 manage.py runserver

where pnpm > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing pnpm...
    npm install -g pnpm
)

if not exist docs/node_modules (
    cd docs && pnpm install
)

cd docs && start cmd /k pnpm run dev

endlocal