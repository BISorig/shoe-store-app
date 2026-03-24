import hashlib

from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def hash_refresh_token(token: str):
    return hashlib.sha256(token.encode()).hexdigest()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_oauth2_scheme(token_url: str):
    return OAuth2PasswordBearer(tokenUrl=token_url)


from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)