from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/sign_in')
async def sign_in():
    pass

@router.post('/sign_up')
async def sign_up():
    pass

@router.post('/change_password')
async def sign_up():
    pass

@router.post('/logout')
async def sign_up():
    pass