from utils.env import get_value
from .base import *

ALLOWED_HOSTS = get_env(env.list, "ALLOWED_HOSTS", [], required=True)

EMAIL_USE_TLS = get_env(env.bool, "MAIL_USE_TLS", True)
EMAIL_HOST = get_env(env.str, "MAIL_SERVER", "smtp.gmail.com")
EMAIL_PORT = get_env(env, "MAIL_PORT", 587)
EMAIL_HOST_USER = get_env(env.str, "MAIL_USER", None)
EMAIL_HOST_PASSWORD = get_env(env.str, "MAIL_PASSWORD", None)

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

CORS_ALLOW_CREDENTIALS = True

DJANGO_REDIS_IGNORE_EXCEPTIONS = False
DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DB_OBJECT = get_env(env.db_url, "DB_URI", {})
DATABASES = {
    "default": {
        "ENGINE": get_value(DB_OBJECT, "ENGINE", "django.db.backends.postgresql"),
        "NAME": get_value(DB_OBJECT, "NAME"),
        "USER": get_value(DB_OBJECT, "USER", "postgres"),
        "PASSWORD": get_value(DB_OBJECT, "PASSWORD", required=True),
        "HOST": get_value(DB_OBJECT, "HOST", required=True),
        "PORT": get_value(DB_OBJECT, "PORT", 5432),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PASSWORD,
        },
    }
}
