from sqlalchemy.orm import Session

from app.setting.model import Setting
from app.setting.schema import SettingDto
from app.util.response import response, Message
from app.util.token_checker import token_checker


@token_checker
def get_settings(**kwargs):
    roll = kwargs.get("roll")
    db: Session = kwargs.get("db")
    if roll != "admin":
        return response(
            message=Message.ACCESS_DENIED.value
        )

    settings = db.query(Setting).order_by(Setting.start_date).all()

    data = [
        SettingDto(
            settingId=str(setting.id),
            startDate=str(setting.start_date),
            endDate=str(setting.end_date),
            ratio=str(setting.ratio),
        ) for setting in settings
    ]

    return response(
        message=Message.SUCCESS.value,
        data=data,
    )
