from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.db.database import get_session
from app.core.security import create_token
from app.services.auth_service import get_user, create_user, authenticate_user

router = APIRouter(tags=["auth"])

@router.post("/register")
def register(
    username: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session),
):
    if get_user(session, username):
        raise HTTPException(status_code=400, detail="User exists")

    user = create_user(session, username, password)
    return {"id": user.id, "username": user.username}

@router.post("/token")
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(get_session),
):
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}