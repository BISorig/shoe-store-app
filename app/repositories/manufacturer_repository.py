from sqlalchemy import select

from app.models import Manufacturer


class ManufacturersRepository:
    def __init__(self, db):
        self.db = db

    def get_all_manufacturers(self):
        stmt = select(Manufacturer)
        result = self.db.execute(stmt).scalars().all()
        return result