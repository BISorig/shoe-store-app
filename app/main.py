from urllib import request

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.exceptions.handlers import register_exception_handlers
from app.routers import auth_router, orders_router, products_router
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

app.include_router(auth_router.router)
app.include_router(products_router.router)
app.include_router(orders_router.router)


app.mount("/static", StaticFiles(directory="app/static", html=True), name="static")

register_exception_handlers(app)

@app.get("/")
def redirect_to_main():
    return RedirectResponse("/login")
