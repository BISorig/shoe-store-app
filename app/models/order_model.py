from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column()
    order_date: Mapped[datetime] = mapped_column()
    delivery_date: Mapped[datetime] = mapped_column()
    article: Mapped[str] = mapped_column()
    receipt_code: Mapped[int] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="orders")

    pickup_point_id: Mapped[int] = mapped_column(ForeignKey("pickup_points.id"))
    pickup_point = relationship("PickupPoint", back_populates="orders")

    items = relationship("OrderItem", back_populates="order")