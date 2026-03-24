from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.params import Cookie
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import FileResponse

from starlette.status import HTTP_409_CONFLICT
from starlette.templating import Jinja2Templates

from app.dependencies.get_current_user import get_current_user
from app.schemas.user_schema import UserCreate
from app.services.auth_service import AuthService
from app.exceptions.exceptions import UserAlreadyExistsError
from app.dependencies.services_factory import get_auth_service

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, service: AuthService = Depends(get_auth_service)):
    try:
        return service.register_user({"email": user.email, "password": user.password})
    except UserAlreadyExistsError:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="User already exists")

@router.get("/login")
def load_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login(response: Response,
          form_data: OAuth2PasswordRequestForm = Depends(),
          auth_service: AuthService = Depends(get_auth_service)
          ):
    user, access_token = auth_service.login(form_data)

    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return {"user": user, "access_token": access_token}


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {}


@router.get("/me")
def read_me(current_user=Depends(get_current_user)):
    return {"user": current_user}
