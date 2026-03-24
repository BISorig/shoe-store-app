from fastapi import Depends, HTTPException, Cookie
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, ExpiredSignatureError, JWTError
from starlette import status

from app.core.security import ALGORITHM, SECRET_KEY, get_oauth2_scheme
from app.dependencies.services_factory import get_user_service
from app.services.user_service import UserService


def get_current_user(access_token: str = Cookie(None),
                     service: UserService = Depends(get_user_service)):
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        user = service.get_user_by_email(email)
        return user
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except AttributeError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
            headers={"WWW-Authenticate": "Bearer"}
        )