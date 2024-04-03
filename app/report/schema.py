from typing import Optional

from pydantic import BaseModel


class ReportVo(BaseModel):
    sdate: Optional[str] = None
    edate: Optional[str] = None


class ReportRowDto(BaseModel):
    day: Optional[str] = ""
    imp: Optional[str] = ""
    click: Optional[str] = ""
    sale: Optional[str] = ""
    order_cnt: Optional[str] = ""
    cancel_cnt: Optional[str] = ""
    revenue: Optional[str] = ""


class ReportSumDto(BaseModel):
    imp: Optional[int] = 0
    click: Optional[int] = 0
    sale: Optional[int] = 0
    order_cnt: Optional[int] = 0
    cancel_cnt: Optional[int] = 0
    revenue: Optional[int] = 0
