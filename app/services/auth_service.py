from sqlalchemy.exc import IntegrityError

from app.core.security import create_access_token
from app.exceptions.exceptions import InvalidCredentialsError, UserAlreadyExistsError
from app.services.user_service import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def register_user(self, user_data):
        try:
            return self.user_service.create_user(user_data)
        except IntegrityError:
            raise UserAlreadyExistsError("User already exists")

    def login(self, user_data):
        user = self.user_service.get_user_by_email(user_data.username)

        if not user or user.password != user_data.password:
            raise InvalidCredentialsError("Invalid credentials")

        access_token = create_access_token({"sub": user.email})

        return user, access_token
