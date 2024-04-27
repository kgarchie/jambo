from django.http import Http404
from rest_framework.authtoken.models import Token
from api.models import Customer
from django.shortcuts import get_object_or_404


def get_auth_token(request) -> str | None:
    header = request.META.get("Authorization")
    if not header:
        return None
    token = header.split(" ")
    if len(token) != 2 or token[0] != "Token" or token[1].strip() == "":
        return None
    return token[1]


def get_user(request) -> (Customer | None, ValueError | Http404 | None):
    token = get_auth_token(request)
    if not token:
        err = ValueError("Authorization Token Not Found Within HTTP Headers")
        return None, err

    try:
        return get_object_or_404(Token, key=token).user, None
    except Http404:
        return None, Http404("User Not Found or is Invalid")
