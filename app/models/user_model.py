from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")

    orders = relationship("Order", back_populates="user")
