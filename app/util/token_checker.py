from functools import wraps
from typing import Callable

import jwt

from app.util.config import ACCESS_TOKEN_SECRET_KEY, ACCESS_TOKEN_ALGORITHM
from app.util.response import response, Message


def token_checker(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs.get("access_token"):
            return response(message=Message.NO_ACCESS_TOKEN.value)
        try:
            payload = jwt.decode(
                jwt=kwargs.get("access_token"),
                key=ACCESS_TOKEN_SECRET_KEY,
                algorithms=ACCESS_TOKEN_ALGORITHM
            )
            auth_id = payload.get("auth_id")
            roll = payload.get("roll")
            return func(*args, **kwargs, auth_id=auth_id, roll=roll)
        except jwt.ExpiredSignatureError:
            return response(message=Message.EXPIRED_ACCESS_TOKEN.value)
        except jwt.exceptions.DecodeError:
            return response(message=Message.WRONG_ACCESS_TOKEN.value)

    return wrapper
