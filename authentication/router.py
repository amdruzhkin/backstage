from fastapi import APIRouter
from .jwt_manager import *
from authentication.schemas import UserSignIn, UserSignUp, UserChangePassword

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/sign_in', status_code=200)
async def sign_in(payload: UserSignIn):
    um = UserManager()
    await um.sign_in(payload)

@router.post('/sign_up', status_code=201)
async def sign_up(payload: UserSignUp):
    um = UserManager()
    await um.sign_up(payload)

@router.put('/change_password')
async def change_password(payload: UserChangePassword, um: UserManager = Depends(get_current_user)):
    await um.change_password()

@router.get('/logout')
async def logout():
    pass