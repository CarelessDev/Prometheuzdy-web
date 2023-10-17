from fastapi import APIRouter

from app.api.rest.auth.router import router as auth_router
from app.api.rest.user.router import router as user_router
from app.api.rest.minecraft.router import router as minecraft_router

router = APIRouter()

router.include_router(auth_router, prefix='/auth', tags=["auth"])
router.include_router(user_router, prefix='/user', tags=["user"])
router.include_router(minecraft_router, prefix='/minecraft', tags=["mc"])