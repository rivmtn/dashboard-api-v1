from typing import Optional

from pydantic import BaseModel


class LoginVo(BaseModel):
    authId: Optional[str] = None
    password: Optional[str] = None


class LoginDto(BaseModel):
    accessToken: Optional[str] = ""
    roll: Optional[str] = ""
