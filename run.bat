@echo off
setlocal

where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3 is not installed. Please download and install Python from:
    echo https://www.python.org/downloads/
    exit /b 1
)

if not exist .\.venv\Scripts\activate.bat (
    python -m venv .venv
    .\.venv\Scripts\python -m pip install -r requirements.txt
)


.\.venv\Scripts\python manage.py makemigrations --no-input
.\.venv\Scripts\python manage.py migrate --no-input

.\.venv\Scripts\python manage.py makemigrations api --no-input
.\.venv\Scripts\python manage.py migrate api --no-input


where pnpm > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing pnpm...
    npm install -g pnpm
)

if not exist docs/node_modules (
    cd docs && pnpm install
)

start cmd /k .\.venv\Scripts\python manage.py runserver
cd docs && start cmd /k pnpm run docs:dev

endlocal