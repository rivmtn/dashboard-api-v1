from datetime import datetime, timedelta

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.setting.model import Setting
from app.setting.schema import SettingVo
from app.util.response import response, Message
from app.util.token_checker import token_checker


@token_checker
def insert_setting(**kwargs):
    roll = kwargs.get("roll")
    db: Session = kwargs.get("db")
    vo: SettingVo = kwargs.get("vo")
    if roll != "admin":
        return response(
            message=Message.ACCESS_DENIED.value
        )
    try:
        existing_settings = db.query(Setting).order_by(Setting.start_date).all()

        # 1. 시작일, 종료일 모두 없을 경우
        if not vo.startDate and not vo.endDate:
            db.query(Setting).delete()
            new_setting = Setting(
                start_date=10000000,
                end_date=99999999,
                ratio=int(vo.ratio),
            )
            db.add(new_setting)

        # 2. 시작일만 있을 경우
        if vo.startDate and not vo.endDate:
            same_setting = db.query(Setting).filter(Setting.start_date == int(vo.startDate)).first()
            if same_setting:
                db.delete(same_setting)
            before_setting = db.query(Setting).filter(Setting.start_date < int(vo.startDate)).order_by(
                desc(Setting.start_date)).first()
            before_setting.end_date = get_previous_date(vo.startDate)
            after_settings = db.query(Setting).filter(Setting.start_date > int(vo.startDate)).all()
            for after_setting in after_settings:
                db.delete(after_setting)
            new_setting = Setting(
                start_date=int(vo.startDate),
                end_date=99999999,
                ratio=int(vo.ratio),
            )
            db.add(new_setting)

        # 3. 종료일만 있을 경우
        if not vo.startDate and vo.endDate:
            same_setting = db.query(Setting).filter(Setting.end_date == int(vo.endDate)).first()
            if same_setting:
                db.delete(same_setting)
            after_setting = db.query(Setting).filter(Setting.end_date > int(vo.endDate)).order_by(
                Setting.end_date).first()
            after_setting.start_date = get_next_date(vo.endDate)
            before_settings = db.query(Setting).filter(Setting.end_date < int(vo.endDate)).all()
            for before_setting in before_settings:
                db.delete(before_setting)
            existing_settings[0].start_date = get_next_date(vo.endDate)
            new_setting = Setting(
                start_date=10000000,
                end_date=int(vo.endDate),
                ratio=int(vo.ratio),
            )
            db.add(new_setting)

        # 4. 시작일, 종료일 모두 있을 경우
        if vo.startDate and vo.endDate:
            between_settings = db.query(Setting).filter(Setting.start_date >= int(vo.startDate),
                                                        Setting.end_date <= int(vo.endDate)).all()
            for between_setting in between_settings:
                db.delete(between_setting)
            before_setting = db.query(Setting).filter(Setting.start_date < int(vo.startDate)).order_by(
                desc(Setting.start_date)).first()
            after_setting = db.query(Setting).filter(Setting.end_date > int(vo.endDate)).order_by(
                Setting.end_date).first()

            if before_setting.start_date == after_setting.start_date and before_setting.end_date == after_setting.end_date:
                new_before_setting = Setting(
                    start_date=before_setting.start_date,
                    end_date=get_previous_date(vo.startDate),
                    ratio=before_setting.ratio,
                )
                db.add(new_before_setting)
                after_setting.start_date = get_next_date(vo.endDate)
            else:
                before_setting.end_date = get_previous_date(vo.startDate)
                after_setting.start_date = get_next_date(vo.endDate)

            new_setting = Setting(
                start_date=int(vo.startDate),
                end_date=int(vo.endDate),
                ratio=int(vo.ratio),
            )
            db.add(new_setting)
        db.commit()
        return response(message=Message.SUCCESS.value)
    except Exception as e:
        db.rollback()
        return response(message=Message.FAIL.value)


def get_previous_date(date_str: str) -> str:
    date_format = "%Y%m%d"
    date_obj = datetime.strptime(date_str, date_format)
    previous_date_obj = date_obj - timedelta(days=1)
    return previous_date_obj.strftime(date_format)


def get_next_date(date_str: str) -> str:
    date_format = "%Y%m%d"
    date_obj = datetime.strptime(date_str, date_format)
    next_date_obj = date_obj + timedelta(days=1)
    return next_date_obj.strftime(date_format)
