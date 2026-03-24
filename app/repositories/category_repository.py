from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Category


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_categories(self):
        stmt = select(Category)
        result = self.db.execute(stmt).scalars().all()
        return result