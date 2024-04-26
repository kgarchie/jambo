#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ
from django.core.management.utils import get_random_secret_key

from utils.env import get_env


def main():
    """Run administrative tasks."""
    env = environ.Env()
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    environ.Env.read_env(env_path)

    secret_key = get_env(env, "SECRET_KEY", None)
    if secret_key is None:
        secret_key = get_random_secret_key()
        with open(env_path, 'a') as f:
            f.write(f'\nSECRET_KEY="{secret_key}"\n')

    os.environ.setdefault('SECRET_KEY', secret_key)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
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
