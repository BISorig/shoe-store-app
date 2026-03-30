from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import PickupPoint


class PickupPointRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_pickup_points(self):
        stmt = select(PickupPoint).order_by(PickupPoint.id)
        return self.db.execute(stmt).scalars().all()
