from fastapi import Request, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette import status
from starlette.responses import RedirectResponse

from app.exceptions.exceptions import DataNotFoundError, InvalidCredentialsError, NotEnoughRights


async def data_not_found_handler(request: Request, exc: DataNotFoundError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={"message": "Data not found."})


async def invalid_credentials_handler(request: Request, exc: InvalidCredentialsError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "Invalid credentials"})


async def not_enough_rights_handler(request: Request, exc: NotEnoughRights) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"message": "Not enough rights"})


async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        return RedirectResponse("/login")
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

async def global_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(DataNotFoundError, data_not_found_handler)
    app.add_exception_handler(InvalidCredentialsError, invalid_credentials_handler)
    app.add_exception_handler(NotEnoughRights, not_enough_rights_handler)
    app.add_exception_handler(Exception, global_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)