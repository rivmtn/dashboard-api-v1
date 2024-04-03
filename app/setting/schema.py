from typing import Optional

from pydantic import BaseModel


class SettingVo(BaseModel):
    settingId: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    ratio: Optional[str] = None


class SettingDto(SettingVo):
    pass
