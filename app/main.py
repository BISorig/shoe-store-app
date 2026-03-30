from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.exceptions.handlers import register_exception_handlers
from app.routers import auth_router, orders_router, products_router

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.include_router(auth_router.router)
app.include_router(products_router.router)
app.include_router(orders_router.router)


app.mount("/static", StaticFiles(directory="app/static", html=True), name="static")

register_exception_handlers(app)


@app.get("/")
def redirect_to_main():
    return RedirectResponse("/login")
