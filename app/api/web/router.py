from fastapi import APIRouter

from app.api.web.auth.router import router as auth_router
from app.api.web.home.router import router as home_router

router = APIRouter()

router.include_router(auth_router, prefix='/auth', tags=["auth"])
router.include_router(home_router, tags=["user"])