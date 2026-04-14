from typing import Annotated
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException
from sqlmodel import Session

from app.core.config import SECRET_KEY, ALGORITHM
from app.core.security import oauth2_scheme
from app.db.database import get_session
from app.services.auth_service import get_user

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_session),
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = get_user(session, username)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user