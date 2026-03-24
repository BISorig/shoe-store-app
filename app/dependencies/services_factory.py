from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.repositories.category_repository import CategoryRepository
from app.repositories.manufacturer_repository import ManufacturersRepository
from app.repositories.order_repository import OrderRepository
from app.repositories.pickup_point_repository import PickupPointRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.supplier_repository import SupplierRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.category_service import CategoryService
from app.services.manufacturer_service import ManufacturerService
from app.services.order_service import OrderService
from app.services.pickup_point_service import PickupPointService
from app.services.supplier_service import SupplierService
from app.services.user_service import UserService

from app.services.product_service import ProductService


def get_user_service(db: Session = Depends(get_db)):
    repository = UserRepository(db=db)
    return UserService(repository)


def get_auth_service(user_service: UserService = Depends(get_user_service)):
    return AuthService(user_service)

def get_products_service(db: Session = Depends(get_db)):
    repository = ProductRepository(db=db)
    return ProductService(repository)

def get_suppliers_service(db: Session = Depends(get_db)):
    repository = SupplierRepository(db=db)
    return SupplierService(repository)

def get_manufacturers_service(db: Session = Depends(get_db)):
    repository = ManufacturersRepository(db=db)
    return ManufacturerService(repository)

def get_category_service(db: Session = Depends(get_db)):
    repository = CategoryRepository(db=db)
    return CategoryService(repository)


def get_orders_service(db: Session = Depends(get_db)):
    repository = OrderRepository(db=db)
    return OrderService(repository)


def get_pickup_points_service(db: Session = Depends(get_db)):
    repository = PickupPointRepository(db=db)
    return PickupPointService(repository)

