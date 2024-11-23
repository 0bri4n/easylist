from fastapi import APIRouter

from .login import router as login_router

router_auth = APIRouter()

router_auth.include_router(login_router, prefix="/auth")
