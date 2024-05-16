import os
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from utils.env import get_env


def time_in_hours(hours) -> int:
    """
    Convert hours to seconds
    :param hours: int
    :return: int
    """
    return hours * 60 * 60


def cache_decorator(func: callable):
    try:
        if os.environ.get("REDIS_URL") is not None:
            return method_decorator(cache_page(time_in_hours(1)))(func)
        else:
            return func
    except Exception as e:
        print(f"Error thrown in cache_decorator: {e}")
        return func
