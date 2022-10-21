from fastapi import HTTPException

from database import get_session
from .models import User
from .schemas import UserSignIn, UserSignUp


class UserManager:
    def __init__(self):
        self.model: User = None

    async def sign_in(self, payload: UserSignIn):
        if payload.login is None and payload.email is None:
            raise HTTPException(status_code=422, detail='Unsupported payload format')
        elif payload.login is not None:
            await self.__sign_in_by_login(payload.login, payload.password)
        elif payload.email is not None:
            await self.__sign_in_by_email(payload.email, payload.password)

        if self.model is None:
            raise HTTPException(status_code=404, detail='User not found')

    async def __sign_in_by_login(self, login: str, password: str):
        with get_session() as db:
            self.model = db.query(User).filter_by(login=login, password=password).first()

    async def __sign_in_by_email(self, email: str, password: str):
        with get_session() as db:
            self.model = db.query(User).filter_by(email=email, password=password).first()

    async def sign_up(self, payload: UserSignUp):
        with get_session() as db:
            try:
                user = User(**payload.dict())
                db.add(user)
                db.commit()
            except Exception as e:
                raise HTTPException(status_code=422, detail=str(e))


    async def change_password(self, previous, new):
        pass

    async def logout(self):
        pass
