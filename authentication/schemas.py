from pydantic import BaseModel


class UserSignIn(BaseModel):
    login: str = None
    email: str = None
    password: str

class UserSignUp(BaseModel):
    login: str
    email: str
    password: str

class UserChangePassword(BaseModel):
    previous: str
    new: str