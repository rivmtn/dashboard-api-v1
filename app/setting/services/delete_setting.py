from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from app.setting.model import Setting
from app.util.response import response, Message
from app.util.token_checker import token_checker


@token_checker
def delete_setting(**kwargs):
    roll = kwargs.get("roll")
    db: Session = kwargs.get("db")
    id = kwargs.get("id")
    if roll != "admin":
        return response(
            message=Message.ACCESS_DENIED.value
        )
    try:
        target_setting = db.query(Setting).filter(Setting.id == id).first()
        count = db.query(func.count(Setting.id)).scalar()

        if target_setting.start_date == 10000000 and target_setting.end_date != 99999999:
            after_setting = db.query(Setting).filter(Setting.start_date > target_setting.end_date).order_by(
                Setting.start_date).first()
            after_setting.start_date = 10000000

        if target_setting.start_date != 10000000 and target_setting.end_date == 99999999:
            before_setting = db.query(Setting).filter(Setting.end_date < target_setting.start_date).order_by(
                desc(Setting.end_date)).first()
            before_setting.end_date = 99999999

        if target_setting.start_date != 10000000 and target_setting.end_date != 99999999:
            before_setting = db.query(Setting).filter(Setting.end_date < target_setting.start_date).order_by(
                Setting.end_date).first()
            before_setting.end_date = target_setting.end_date

        db.delete(target_setting)

        if count == 1:
            db.add(
                Setting(
                    start_date=10000000,
                    end_date=99999999,
                    ratio=100,
                )
            )
        db.commit()

        return response(message=Message.SUCCESS.value)
    except Exception as e:
        return response(message=Message.FAIL.value)
