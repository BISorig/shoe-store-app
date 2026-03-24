from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class PickupPoint(Base):
    __tablename__ = "pickup_points"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column()

    orders = relationship("Order", back_populates="pickup_point")

