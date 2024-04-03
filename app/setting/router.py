from typing import Annotated, Optional

from fastapi import APIRouter, Body
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.setting.schema import SettingVo
from app.setting.services.delete_setting import delete_setting
from app.setting.services.get_settings import get_settings
from app.setting.services.insert_setting import insert_setting
from app.util.database import get_db

router = APIRouter()


@router.get(path="/setting")
async def member(access_token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))],
                 db: Session = Depends(get_db)):
    result = get_settings(access_token=access_token, db=db)
    return result


@router.post(path="/setting")
async def _(access_token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))],
            db: Session = Depends(get_db),
            vo: SettingVo = Body(SettingVo())):
    result = insert_setting(access_token=access_token, db=db, vo=vo)
    return result


@router.delete(path="/setting")
async def _(access_token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))],
            db: Session = Depends(get_db),
            id: Optional[str] = None):
    result = delete_setting(access_token=access_token, db=db, id=id)
    return result
