from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Supplier


class SupplierRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_suppliers(self):
        stmt = select(Supplier)
        result = self.db.execute(stmt).scalars().all()
        return result