#!/usr/bin/env bash

if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please download and install Python from:"
    echo "https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    sudo apt install python"$PYTHON_VERSION"-venv
    python3 -m venv venv
fi

source venv/bin/activate

sudo apt-get install libpq-dev python3-dev

pip3 install -r requirements.txt

python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input
python3 manage.py makemigrations api --no-input
python3 manage.py migrate api --no-input
python3 manage.py runserver &


if ! command -v node &>/dev/null; then
    echo "Node.js is not installed. Please download and install Node.js from:"
    echo "https://nodejs.org/en/download/"
    deactivate
    exit 1
fi


if ! command -v pnpm &>/dev/null; then
    echo "pnpm is not installed. Installing pnpm..."
    npm install -g pnpm
fi


if [ ! -d "docs/node_modules" ]; then
    echo "Installing dependencies..."
    cd docs && pnpm install || echo "docs directory not found. Please run the script from the root directory of the project." && exit 1
fi

pnpm run docs:dev &

deactivate