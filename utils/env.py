import os
from typing import Any
from django.core.management.utils import get_random_secret_key
from environ import ImproperlyConfigured


def get_redis_url(env: callable) -> str | None:
    """
    Get the Redis URL from the environment variables.
    This method does not include the password because special characters may need to be escaped.
    :param env: environ Object
    :return: Redis URL
    """
    redis_url = get_env(env, "REDIS_URL", None)
    redis_user = get_env(env, "REDIS_USER", None)

    if redis_url is not None and redis_user is not None:
        [first, second] = redis_url.split("://")
        redis_url = f"{first}://{redis_user}@{second}"

    return redis_url


def get_redis_password(env: callable) -> str:
    """
    Get the Redis password from the environment variables
    :param env:
    :return:
    """
    try:
        return get_env(env, "REDIS_PASSWORD")
    except ImproperlyConfigured:
        return ""


def get_env(
    env: callable, name: str, default: any = None, required: bool = False
) -> str | dict | list | None:
    """
    Get the environment variable
    :param required: If the environment variable is required, will throw an error if not found
    :param env: environ Object, or Function
    :param name: Name of the environment variable
    :param default: Default value if the environment variable is not found
    :return: Value of the environment variable, Value could also be the parsed version from env
    """

    try:
        value = env(name)
    except ImproperlyConfigured:
        value = None
        pass

    if isinstance(value, str):
        if value.strip() == "":
            value = None

    if isinstance(value, dict) or isinstance(value, list):
        if len(value) == 0:
            value = None

    if required and value is None:
        raise ImproperlyConfigured(f"Env variable {name} is required")

    return value or default


def get_secret_key(env: callable, base: str | None = None) -> str:
    if base is None:
        base = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")

    secret_key = get_env(env, "SECRET_KEY", None)
    if secret_key is None:
        secret_key = get_random_secret_key()
        with open(base / ".env", "a") as f:
            f.write(f'\nSECRET_KEY="{secret_key}"\n')

    os.environ.setdefault("SECRET_KEY", secret_key)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    return secret_key


def get_value(_dict: dict, key: str, default: Any = None, required: bool = False) -> Any:
    """
    Get the value from the dictionary
    :param _dict: Dictionary
    :param key: Key
    :return: Value
    """
    try:
        return _dict[key]
    except Exception:
        if required:
            raise ImproperlyConfigured(f"Key {key} is required in the dictionary")
        return default
