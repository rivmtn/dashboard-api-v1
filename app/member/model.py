from sqlalchemy import Column, Integer, String, func, DateTime

from app.util.database import Base


class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="멤버id")

    roll = Column(String(5), nullable=False, server_default="user", doc="권한")  # or admin
    auth_id = Column(String(20), nullable=False, unique=True, doc="아이디")
    password = Column(String(60), nullable=False, doc="비밀번호")
    api_key = Column(String(50), doc="API키")
    created_at = Column(DateTime, server_default=func.current_timestamp(), doc="생성일")
