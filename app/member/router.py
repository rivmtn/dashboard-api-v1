from typing import Annotated, Optional

from fastapi import APIRouter, Body
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.member.schema import MemberVo
from app.member.services.delete_member import delete_member
from app.member.services.get_members import get_members
from app.member.services.insert_member import insert_member
from app.member.services.update_member import update_member
from app.util.database import get_db

router = APIRouter()


@router.get(path="/member")
async def member(access_token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))],
                 db: Session = Depends(get_db)):
    result = get_members(access_token=access_token, db=db)
    return result


@router.post(path="/member")
async def member(access_token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))],
                 db: Session = Depends(get_db),
                 vo: MemberVo = Body(MemberVo())):
    result = insert_member(access_token=access_token, db=db, vo=vo)
    return result


@router.put(path="/member")
async def member(access_token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))],
                 db: Session = Depends(get_db),
                 vo: MemberVo = Body(MemberVo())):
    result = update_member(access_token=access_token, db=db, vo=vo)
    return result


@router.delete(path="/member")
async def member(access_token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))],
                 db: Session = Depends(get_db),
                 id: Optional[str] = None):
    result = delete_member(access_token=access_token, db=db, id=id)
    return result
