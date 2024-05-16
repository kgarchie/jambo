from .base import *

DB_OBJECT = get_env(env.db_url, "DATABASE_URI", None)

if DB_OBJECT:
    DATABASES = {"default": DB_OBJECT}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

if REDIS_URL:
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

DJANGO_REDIS_IGNORE_EXCEPTIONS = True
DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True

CORS_ALLOW_CREDENTIALS = True
ALLOWED_HOSTS = get_env(env.list, "ALLOWED_HOSTS", "*")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
