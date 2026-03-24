from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from app.db.base import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    products = relationship("Product", back_populates="category")