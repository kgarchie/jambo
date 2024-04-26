from environ import ImproperlyConfigured


def get_redis_url(env: callable) -> str | None:
    """
    Get the Redis URL from the environment variables.
    This method does not include the password because it may need to be escaped.
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


def get_env(env: callable, name: str, default: any = None, required: bool = False) -> str | dict | list | None:
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

    if required and value is None:
        raise ImproperlyConfigured(f"Env variable {name} is required")

    return value or default
