from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.base import Base


class Manufacturer(Base):
    __tablename__ = "manufacturers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    products = relationship("Product", back_populates="manufacturer")
