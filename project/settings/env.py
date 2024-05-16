import environ
from os.path import join
from pathlib import Path
from utils.env import get_env, get_secret_key

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DOCKER_ENV = get_env(env, "DOCKER_ENV", False)

if not DOCKER_ENV:
    environ.Env.read_env(join(BASE_DIR, ".env"))
else:
    # environ.Env.read_env(join(BASE_DIR, ".env.docker"))
    pass

DEBUG = get_env(env.bool, "DEBUG", False)

SECRET_KEY = get_secret_key(env, BASE_DIR)
