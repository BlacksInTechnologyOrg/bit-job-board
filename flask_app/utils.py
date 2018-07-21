import secrets


def hashid():
    return secrets.token_hex(nbytes=16)