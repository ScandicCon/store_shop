from sqlmodel import Session, select

from app.db.models import User
from app.core.security import verify_password, DUMMY_HASH, hash_password

def get_user(session: Session, username: str):
    return session.exec(select(User).where(User.username == username)).first()

def create_user(session: Session, username: str, password: str):
    user = User(username=username, hashed_password=hash_password(password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def authenticate_user(session: Session, username: str, password: str):
    user = get_user(session, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False

    if not verify_password(password, user.hashed_password):
        return False

    return user