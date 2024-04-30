#!/usr/bin/env bash

python manage.py collectstatic --noinput

# force sleep to wait for db to be ready
echo "Forcing sleep 15s to wait for db to be ready..."

sleep 10

python manage.py makemigrations --noinput

python manage.py makemigrations api --no-input
python manage.py migrate api --no-input

python manage.py migrate --noinput

gunicorn project.wsgi:application --bind 0.0.0.0:8000
