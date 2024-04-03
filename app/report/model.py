from sqlalchemy import Column, Integer

from app.util.database import Base


class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="현황id")

    day = Column(Integer, nullable=False, unique=True, doc="날짜")
    imp = Column(Integer, nullable=False, doc="노출")
    click = Column(Integer, nullable=False, doc="클릭수")
    sale = Column(Integer, nullable=False, doc="매출")
    order_cnt = Column(Integer, nullable=False, doc="주문수")
    cancel_cnt = Column(Integer, nullable=False, doc="취소수")
    revenue = Column(Integer, nullable=False, doc="수익")
