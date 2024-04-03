from sqlalchemy import Column, Integer

from app.util.database import Base


class Setting(Base):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="설정id")
    start_date = Column(Integer, doc="시작일")
    end_date = Column(Integer, doc="종료일")
    ratio = Column(Integer, doc="비율(%)")


if __name__ == '__main__':
    a = {
        "start_date": 10000000,
        "end_date": 99999999,
        "ratio": 100,
    }
    b = {
        "start_date": 20240327,
        "end_date": None,
        "ratio": 90,
    }
    c = [
        {
            "start_date": 10000000,
            "end_date": 20240326,
            "ratio": 100,
        },
        {
            "start_date": 20240327,
            "end_date": 99999999,
            "ratio": 90,
        }
    ]
    d = {
        "start_date": 20240401,
        "end_date": None,
        "ratio": 80,
    }
    e = [
        {
            "start_date": 10000000,
            "end_date": 20240326,
            "ratio": 100,
        },
        {
            "start_date": 20240327,
            "end_date": 20240331,
            "ratio": 90,
        },
        {
            "start_date": 20240401,
            "end_date": 99999999,
            "ratio": 80,
        }
    ]
    f = [
        {
            "start_date": 10000000,
            "end_date": 20240331,
            "ratio": 100,
        },
        {
            "start_date": 20240401,
            "end_date": 99999999,
            "ratio": 80,
        }
    ]
    g = {
        "start_date": 20240315,
        "end_date": 20240425,
        "ratio": 70,
    }
    h = [
        {
            "start_date": 10000000,
            "end_date": 20240314,
            "ratio": 100,
        },
        {
            "start_date": 20240315,
            "end_date": 20240425,
            "ratio": 70,
        },
        {
            "start_date": 20240426,
            "end_date": 99999999,
            "ratio": 80,
        }
    ]
