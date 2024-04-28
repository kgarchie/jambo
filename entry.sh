#!/usr/bin/env bash

python manage.py collectstatic --noinput

python manage.py makemigrations --noinput

python manage.py makemigrations api --no-input
python manage.py migrate api --no-input

python manage.py migrate --noinput

gunicorn django_project.wsgi:application --bind 0.0.0.0:8000
