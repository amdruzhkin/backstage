from fastapi import Depends
from fastapi.security import HTTPBearer
from .user_manager import UserManager

SCHEME = HTTPBearer()

def get_current_user(token: str = Depends(SCHEME)) -> UserManager:
    print(token)
