from django.core.mail import send_mail as _send_mail
from environ import environ

from utils.env import get_env


def send_mail(destination, subject, body):
    """
    Send an email to a recipient
    """
    env = environ.Env()
    _send_mail(subject=subject, message=body, recipient_list=[destination],
               from_email=get_env(env, "EMAIL_HOST_USER", None))
