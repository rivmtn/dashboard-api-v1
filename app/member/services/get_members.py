from sqlalchemy.orm import Session

from app.member.model import Member
from app.member.schema import MemberDto
from app.util.response import response, Message
from app.util.time import time_to_date
from app.util.token_checker import token_checker


@token_checker
def get_members(**kwargs):
    roll = kwargs.get("roll")
    db: Session = kwargs.get("db")
    if roll != "admin":
        return response(
            message=Message.ACCESS_DENIED.value
        )

    members = db.query(Member).order_by(Member.created_at).all()

    data = [
        MemberDto(
            memberId=str(member.id),
            roll=member.roll,
            authId=member.auth_id,
            apiKey=member.api_key,
            createdAt=time_to_date(member.created_at),
        ) for member in members
    ]

    return response(
        message=Message.SUCCESS.value,
        data=data,
    )
