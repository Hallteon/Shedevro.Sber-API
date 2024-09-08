from typing import Optional
from fastapi_users import schemas
from pydantic import BaseModel


class RoleReadSchema(BaseModel):
    id: int
    name: str
    role_type: str


class UserReadSchema(schemas.BaseUser[int]):
    id: int
    email: str
    lastname: str
    firstname: str
    surname: str

    # role: Optional[RoleReadSchema] = None

    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class UserCreateSchema(schemas.BaseUserCreate):
    email: str

    lastname: str
    firstname: str
    surname: str
    password: str

    role_id: Optional[int] = None

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
