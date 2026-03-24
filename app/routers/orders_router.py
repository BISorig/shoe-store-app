from datetime import datetime

from fastapi import APIRouter, Depends, Form, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.dependencies.get_current_user import get_current_user
from app.dependencies.services_factory import get_orders_service, get_pickup_points_service, get_user_service
from app.exceptions.exceptions import NotEnoughRights
from app.schemas.order_schema import OrderCreate, OrderUpdate

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(prefix="/orders", tags=["orders"])

ADMIN_ROLE = "Администратор"
MANAGER_ROLE = "Менеджер"


def require_manager_or_admin(user) -> None:
    if user.role.name not in [ADMIN_ROLE, MANAGER_ROLE]:
        raise NotEnoughRights()


def require_admin(user) -> None:
    if user.role.name != ADMIN_ROLE:
        raise NotEnoughRights()


@router.get("/", response_class=HTMLResponse)
def get_orders(
    request: Request,
    current_user=Depends(get_current_user),
    orders_service=Depends(get_orders_service),
    pickup_points_service=Depends(get_pickup_points_service),
    user_service=Depends(get_user_service),
):
    require_manager_or_admin(current_user)

    template_data = {
        "request": request,
        "orders": orders_service.get_all_orders(),
        "full_name": current_user.full_name,
        "user_role": current_user.role.name,
    }

    if current_user.role.name == ADMIN_ROLE:
        template_data["pickup_points"] = pickup_points_service.get_all_pickup_points()
        template_data["users"] = user_service.get_all_users()

    return templates.TemplateResponse("orders.html", template_data)


@router.post("/")
def create_order(
    article: str = Form(...),
    status: str = Form(...),
    pickup_point_id: int = Form(...),
    order_date: datetime = Form(...),
    delivery_date: datetime = Form(...),
    user_id: int = Form(...),
    receipt_code: int = Form(...),
    current_user=Depends(get_current_user),
    orders_service=Depends(get_orders_service),
):
    require_admin(current_user)

    order = OrderCreate(
        article=article,
        status=status,
        pickup_point_id=pickup_point_id,
        order_date=order_date,
        delivery_date=delivery_date,
        user_id=user_id,
        receipt_code=receipt_code,
    )
    return orders_service.create_order(order.model_dump())


@router.put("/{order_id}")
def update_order(
    order_id: int,
    article: str = Form(...),
    status: str = Form(...),
    pickup_point_id: int = Form(...),
    order_date: datetime = Form(...),
    delivery_date: datetime = Form(...),
    user_id: int = Form(...),
    receipt_code: int = Form(...),
    current_user=Depends(get_current_user),
    orders_service=Depends(get_orders_service),
):
    require_admin(current_user)

    order = OrderUpdate(
        article=article,
        status=status,
        pickup_point_id=pickup_point_id,
        order_date=order_date,
        delivery_date=delivery_date,
        user_id=user_id,
        receipt_code=receipt_code,
    )
    return orders_service.update_order(order_id, order.model_dump())


@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    current_user=Depends(get_current_user),
    orders_service=Depends(get_orders_service),
):
    require_admin(current_user)
    orders_service.delete_order(order_id)
    return {"message": "Order deleted"}
