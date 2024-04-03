import jwt
from sqlalchemy.orm import Session

from app.auth.schema import LoginVo, LoginDto
from app.member.model import Member
from app.util.auth import verify_password
from app.util.config import ACCESS_TOKEN_SECRET_KEY, ACCESS_TOKEN_ALGORITHM
from app.util.response import response, Message


def login(**kwargs):
    db: Session = kwargs.get("db")
    vo: LoginVo = kwargs.get("vo")
    member = db.query(Member).filter(Member.auth_id == vo.authId).first()
    if not member:
        return response(
            message=Message.WRONG_ID.value,
        )
    if not verify_password(plain_password=vo.password, hashed_password=member.password):
        return response(
            message=Message.WRONG_PASSWORD.value,
        )
    access_token = jwt.encode(
        payload=dict(
            # exp=datetime.now(timezone('Asia/Seoul')) + timedelta(hours=10),
            auth_id=member.auth_id,
            roll=member.roll
        ),
        key=ACCESS_TOKEN_SECRET_KEY,
        algorithm=ACCESS_TOKEN_ALGORITHM
    )
    data: LoginDto = LoginDto(
        accessToken=access_token,
        roll=member.roll
    )
    return response(
        message=Message.SUCCESS.value,
        data=data,
    )
