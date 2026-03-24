from app.models import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_data) -> User:
        user = User(**user_data)
        return self.repository.create_user(user)

    def get_all_users(self):
        return self.repository.get_all_users()

    def get_user_by_id(self, user_id: int) -> User:
        return self.repository.get_user_by_id(user_id)

    def delete_user(self, user_id: int):
        return self.repository.delete_user(user_id)

    def get_user_by_email(self, email: str):
        return self.repository.get_user_by_email(email)

    def update_user_role(self, user_id: int, role: str):
        return self.repository.update_user_role(user_id, role)