from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User) -> User:
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError:
            self.db.rollback()
            raise

    def get_all_users(self):
        stmt = select(User)
        users = self.db.execute(stmt).scalars().all()
        return users

    def get_user_by_id(self, user_id: int) -> User:
        stmt = select(User).where(User.id == user_id)
        user = self.db.execute(stmt).scalars().first()
        return user

    def get_user_by_email(self, email: str) -> User:
        stmt = select(User).where(User.email == email)
        user = self.db.execute(stmt).scalars().first()
        return user

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        user.is_deleted = True
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user_role(self, user_id: int, role: str):
        user = self.get_user_by_id(user_id)
        user.role = role
        self.db.commit()
        self.db.refresh(user)
        return user

