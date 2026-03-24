from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    discount: Mapped[int] = mapped_column()
    image_path: Mapped[str] = mapped_column()

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

    manufacturer_id: Mapped[int] = mapped_column(ForeignKey("manufacturers.id"))
    manufacturer = relationship("Manufacturer", back_populates="products")

    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"))
    supplier = relationship("Supplier", back_populates="products")
