from enum import Enum

from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse


def response(message=None, data=None, **kwargs):
    return JSONResponse(content=jsonable_encoder(obj=dict(
        message=message,
        data=data,
        **kwargs,
    )))


class Message(Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    NO_ACCESS_TOKEN = "NO_ACCESS_TOKEN"
    EXPIRED_ACCESS_TOKEN = "EXPIRED_ACCESS_TOKEN"
    WRONG_ACCESS_TOKEN = "WRONG_ACCESS_TOKEN"
    ACCESS_DENIED = "ACCESS_DENIED"
    DUPLICATED_ID = "DUPLICATED_ID"
    WRONG_ID = "WRONG_ID"
    WRONG_PASSWORD = "WRONG_PASSWORD"
    WRONG_API_KEY = "WRONG_API_KEY"
