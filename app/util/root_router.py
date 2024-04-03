from fastapi import APIRouter

from app.auth.router import router as auth_router
from app.member.router import router as member_router
from app.report.router import router as report_router
from app.setting.router import router as setting_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(member_router)
router.include_router(report_router)
router.include_router(setting_router)
