from django.contrib.auth.models import User
from django.http import Http404
from api.models import Customer, Token
from django.shortcuts import get_object_or_404


def get_auth_token(request) -> str | None:
    header = request.META.get("Authorization")
    if header is None:
        header = request.META.get("HTTP_AUTHORIZATION")
    if not header:
        return None
    token = header.split(" ")
    if len(token) != 2 or token[0] != "Bearer" or token[1].strip() == "":
        return None
    return token[1]


def get_user_from_request(request) -> (User | None, ValueError | Http404):
    token = get_auth_token(request)
    if not token:
        err = ValueError("Authorization Token Not Found Within HTTP Headers")
        return None, err

    try:
        return get_object_or_404(Token, key=token).user, None
    except Http404:
        return None, Http404("User Not Found or is Invalid")


def get_customer_from_request(request) -> (Customer | None, None | ValueError | Http404):
    token = get_auth_token(request)
    if not token:
        err = ValueError("Authorization Token Not Found Within HTTP Headers")
        return None, err

    try:
        return get_object_or_404(Token, key=token).customer, None
    except Http404:
        return None, Http404("Customer Not Found or is Invalid")
