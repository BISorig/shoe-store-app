import os.path
import shutil

from fastapi import APIRouter, Depends, File, Form, Request, UploadFile
from sqlalchemy.sql.functions import user
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from unicodedata import category

from app.dependencies.get_current_user import get_current_user
from app.dependencies.services_factory import get_products_service, get_suppliers_service, get_manufacturers_service, \
    get_category_service
from app.schemas.product_schema import ProductUpdate

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_class=HTMLResponse)
def get_products(request: Request,
                 current_user = Depends(get_current_user),
                 products_service = Depends(get_products_service),
                 suppliers_service = Depends(get_suppliers_service),
                 manufacturers_service = Depends(get_manufacturers_service),
                 category_service = Depends(get_category_service)):
    products = products_service.get_all_products()

    for product in products:
        if product.image_path is None:
            product.image_path = "picture.png"
    template_dict = {"request": request,
                     "products": products,
                     "full_name": current_user.full_name,
                     "user_role": current_user.role.name}

    if current_user.role.name in ["Администратор", "Менеджер"]:
        suppliers = suppliers_service.get_all_suppliers()
        template_dict["suppliers"] = suppliers

    if current_user.role.name == "Администратор":
        manufacturers = manufacturers_service.get_all_manufacturers()
        template_dict["manufacturers"] = manufacturers

        categories = category_service.get_all_categories()
        template_dict["categories"] = categories

    return templates.TemplateResponse("products.html", template_dict)

@router.get("/guest", response_class=HTMLResponse)
def get_guest_products(request: Request, products_service = Depends(get_products_service)):
    products = products_service.get_all_products()
    for product in products:
        if product.image_path is None:
            product.image_path = "picture.png"
    return templates.TemplateResponse("products.html", {"request": request,
                                                        "products": products,
                                                        "full_name": "",
                                                        "user_role": "Гость"})

@router.put("/{product_id}")
def update_product(product_id: int,
                   name: str = Form(...), 
                   category_id: int = Form(...),
                   description: str = Form(...),
                   manufacturer_id: int = Form(...),
                   supplier_id: int = Form(...),
                   price: float = Form(...),
                   quantity: int = Form(...),
                   image: UploadFile = File(None),
                   product_service = Depends(get_products_service)):
    if image:
        filename = f"/static/images/{image.filename}"
        with open(filename, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_path = image.filename
    else:
        image_path = None

    product = ProductUpdate(name=name,
                            category_id=category_id,
                            description=description,
                            manufacturer_id=manufacturer_id,
                            supplier_id=supplier_id,
                            price=price,
                            quantity=quantity,
                            image_path=image_path)
    return product_service.update_product(product.model_dump(), product_id)

@router.post("/")
def create_product(name: str = Form(...),
                   category_id: int = Form(...),
                   description: str = Form(...),
                   manufacturer_id: int = Form(...),
                   supplier_id: int = Form(...),
                   price: float = Form(...),
                   quantity: int = Form(...),
                   image: UploadFile = File(None),
                   product_service = Depends(get_products_service)):
    filename = f"static/images/{image.filename}" if image else None
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    product_data = {
        "name": name,
        "category_id": category_id,
        "description": description,
        "manufacturer_id": manufacturer_id,
        "supplier_id": supplier_id,
        "price": price,
        "quantity": quantity,
        "image_path": image.filename
    }
    return product_service.create_product(product_data)