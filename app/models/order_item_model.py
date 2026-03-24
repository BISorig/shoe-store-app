from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column()

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    order = relationship("Order", back_populates="items")

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product = relationship("Product")
