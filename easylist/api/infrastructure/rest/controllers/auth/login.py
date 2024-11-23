from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from easylist.api.application.dtos.login_dto import LoginDTO
from easylist.api.application.use_cases.auth_usecase import AuthUseCase

from .dependencies import get_auth_use_case

router = APIRouter()


@router.post("/login", response_model=str)
def login(login_data: LoginDTO, auth_use_case: Annotated[AuthUseCase, Depends(get_auth_use_case)]) -> str:
    token = auth_use_case.authenticate(login_data)
    if not token:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return token
