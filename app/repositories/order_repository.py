from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.exceptions.exceptions import DataNotFoundError, InvalidEnteredDataError
from app.models import Order, OrderItem


class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_orders(self):
        stmt = (
            select(Order)
            .options(joinedload(Order.user), joinedload(Order.pickup_point))
            .order_by(Order.id)
        )
        return self.db.execute(stmt).scalars().all()

    def create_order(self, data: dict):
        order = Order(**data)
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def update_order(self, order_id: int, data: dict):
        stmt = select(Order).where(Order.id == order_id)
        order = self.db.execute(stmt).scalars().first()

        if order is None:
            raise DataNotFoundError()

        for key, value in data.items():
            if value is not None:
                setattr(order, key, value)

        self.db.commit()
        self.db.refresh(order)
        return order

    def delete_order(self, order_id: int):
        stmt = select(Order).where(Order.id == order_id)
        order = self.db.execute(stmt).scalars().first()

        if order is None:
            raise DataNotFoundError()

        has_items_stmt = select(OrderItem).where(OrderItem.order_id == order_id).limit(1)
        has_items = self.db.execute(has_items_stmt).scalars().first()
        if has_items is not None:
            raise InvalidEnteredDataError()

        self.db.delete(order)
        self.db.commit()
