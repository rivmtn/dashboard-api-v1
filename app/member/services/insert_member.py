from sqlalchemy.orm import Session

from app.member.model import Member
from app.member.schema import MemberVo
from app.util.auth import generate_hashed_password
from app.util.response import response, Message
from app.util.token_checker import token_checker


@token_checker
def insert_member(**kwargs):
    roll = kwargs.get("roll")
    db: Session = kwargs.get("db")
    vo: MemberVo = kwargs.get("vo")

    if roll != "admin":
        return response(
            message=Message.ACCESS_DENIED.value
        )
    try:
        auth_id_exists = db.query(Member).filter(Member.auth_id == vo.authId).first()
        if auth_id_exists:
            return response(
                message=Message.DUPLICATED_ID.value
            )

        new_member = Member(
            roll=vo.roll,
            auth_id=vo.authId,
            password=generate_hashed_password(password=vo.password),
            api_key=vo.apiKey,
        )
        db.add(new_member)
        db.commit()
        return response(message=Message.SUCCESS.value)
    except Exception as e:
        db.rollback()
        return response(message=Message.FAIL.value)
