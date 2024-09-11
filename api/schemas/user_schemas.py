from typing import Optional
from fastapi_users import schemas
from pydantic import BaseModel


class RoleReadSchema(BaseModel):
    id: int
    name: str

# Companies schemes

class ProviderReadSchema(BaseModel):
    id: int
    email: str
    name: str

    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True
        populate_by_name = True


class ProviderAuthReadSchema(schemas.BaseUser[int]):
    id: int
    email: str
    name: str

    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True
        populate_by_name = True


class ProviderCreateSchema(schemas.BaseUserCreate):
    email: str
    name: str
    description: str

    password: str

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

# Companies schemes

class CompanyReadSchema(BaseModel):
    id: int
    email: str
    name: str

    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True
        populate_by_name = True


class CompanyAuthReadSchema(schemas.BaseUser[int]):
    id: int
    email: str
    name: str

    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True
        populate_by_name = True


class CompanyCreateSchema(schemas.BaseUserCreate):
    email: str
    name: str
    description: str

    password: str

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


# Student schemes

class StudentReadSchema(BaseModel):
    id: int
    email: str
    lastname: str
    firstname: str
    surname: str
    role: RoleReadSchema
    role_id: int

    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True
        populate_by_name = True


class StudentAuthReadSchema(schemas.BaseUser[int]):
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
        from_attributes = True
        populate_by_name = True


class StudentCreateSchema(schemas.BaseUserCreate):
    email: str

    lastname: str
    firstname: str
    surname: str
    password: str

    role_id: Optional[int] = None

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
