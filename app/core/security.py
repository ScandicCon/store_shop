from datetime import datetime, timedelta, timezone
import jwt
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer

from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

password_hasher = PasswordHash.recommended()
DUMMY_HASH = password_hasher.hash("DUMMY_PASSWORD")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_value: str) -> bool:
    return password_hasher.verify(plain_password, hashed_value)

def hash_password(password: str) -> str:
    return password_hasher.hash(password)

def create_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)