from typing import Annotated
from fastapi import APIRouter, Depends

from app.api.deps import get_current_user
from app.db.models import User

router = APIRouter(tags=["users"])

@router.get("/users/me")
def me(user: Annotated[User, Depends(get_current_user)]):
    return user