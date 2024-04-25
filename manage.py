#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ
from django.core.exceptions import ImproperlyConfigured
from django.core.management.utils import get_random_secret_key

env = environ.Env(DEBUG=(bool, False))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    try:
        secret_key = env('SECRET_KEY')

        if secret_key.strip() == '':
            raise ImproperlyConfigured('SECRET_KEY cannot be blank')
    except ImproperlyConfigured:
        secret_key = get_random_secret_key()
        with open(os.path.join(BASE_DIR, '.env'), 'a') as f:
            f.write(f'\nSECRET_KEY="{secret_key}"\n')

    os.environ.setdefault('SECRET_KEY', secret_key)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
