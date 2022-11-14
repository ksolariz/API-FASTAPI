from fastapi import APIRouter, HTTPException

from schemas import UserCreateInput, Default_message
from services import UserService

user_router = APIRouter(prefix='/user')

@user_router.post('/create',response_model = Default_message)
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.user_create(name=user_input.name)
        return Default_message(message='success')
    except Exception as error:
        raise HTTPException(400,detail=str(error))
        