from fastapi import Depends, HTTPException

from app.dependencies.get_current_user import get_current_user
from app.exceptions.exceptions import NotEnoughRights


def require_role(required_role: str):
    def role_checker(user = Depends(get_current_user)):
        if user.role != required_role:
            raise NotEnoughRights()
        return user
    return role_checker