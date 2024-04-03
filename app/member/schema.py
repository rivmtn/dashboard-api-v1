from typing import Optional

from pydantic import BaseModel


class MemberVo(BaseModel):
    memberId: Optional[str] = None
    roll: Optional[str] = None
    authId: Optional[str] = None
    password: Optional[str] = None
    apiKey: Optional[str] = None
    createdAt: Optional[str] = None


class MemberDto(MemberVo):
    pass
