from fastapi import APIRouter
from auth_setup import auth_backend, fastapi_users
from api.schemas.user_schemas import UserReadSchema, UserCreateSchema


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/users',
    tags=['Users'],
)

router.include_router(
    fastapi_users.get_register_router(UserReadSchema, UserCreateSchema),
    prefix='/users',
    tags=['Users'],
)