from sqlalchemy import select
from sqlalchemy.orm import Session

from app.exceptions.exceptions import DataNotFoundError
from app.models.product_model import Product


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update_product(self, data: dict, product_id: int):
        stmt = select(Product).where(Product.id == product_id)
        product = self.db.execute(stmt).scalars().first()
        for key, value in data.items():
            if value is not None:
                setattr(product, key, value)
        self.db.commit()
        self.db.refresh(product)
        return product

    def create_product(self, data: dict):
        product = Product(**data)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_all_products(self):
        stmt = select(Product).order_by(Product.id)
        products = self.db.execute(stmt).scalars().all()
        return products

    def delete(self, product: Product):
        self.db.delete(product)
        self.db.commit()

    def delete_product(self, product_id: int):
        stmt = select(Product).where(Product.id == product_id)
        product = self.db.execute(stmt).scalars().first()

        if product is None:
            raise DataNotFoundError()

        self.db.delete(product)
        self.db.commit()
