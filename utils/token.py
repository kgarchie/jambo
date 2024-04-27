def get_auth_token(request) -> str | None:
    header = request.META.get("Authorization")
    if not header:
        return None
    token = header.split(" ")
    if len(token) != 2 or token[0] != "Token" or token[1].strip() == "":
        return None
    return token[1]
