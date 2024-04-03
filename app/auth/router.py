from fastapi import APIRouter, Body
from fastapi import Depends
from sqlalchemy.orm import Session

from app.auth.schema import LoginVo
from app.auth.services.login import login
from app.util.database import get_db

router = APIRouter()


@router.post(path="/login")
async def _(db: Session = Depends(get_db),
            vo: LoginVo = Body(LoginVo())):
    result = login(db=db, vo=vo)
    return result
