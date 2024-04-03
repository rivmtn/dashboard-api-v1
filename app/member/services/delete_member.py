from sqlalchemy.orm import Session

from app.member.model import Member
from app.util.response import response, Message
from app.util.token_checker import token_checker


@token_checker
def delete_member(**kwargs):
    roll = kwargs.get("roll")
    db: Session = kwargs.get("db")
    id = kwargs.get("id")

    if roll != "admin":
        return response(
            message=Message.ACCESS_DENIED.value
        )
    try:
        member = db.query(Member).filter(Member.id == int(id)).first()
        db.delete(member)
        db.commit()
        return response(message=Message.SUCCESS.value)
    except Exception as e:
        db.rollback()
        return response(message=Message.FAIL.value)
