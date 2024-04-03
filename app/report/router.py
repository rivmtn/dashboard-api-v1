from typing import Annotated, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.report.services.get_reports import get_reports
from app.util.database import get_db

router = APIRouter()



@router.get(path="/report")
async def _(access_token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))],
            db: Session = Depends(get_db),
            sdate: Optional[str] = None,
            edate: Optional[str] = None):
    result = get_reports(access_token=access_token, db=db, sdate=sdate, edate=edate)
    return result
