from typing import Optional
from fastapi_users import schemas
from pydantic import BaseModel


class CategoryScheme(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
        populate_by_name = True


class PracticeCategorySchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
        populate_by_name = True


class CompanyReadSchema(BaseModel):
    id: int
    name: str
    category: Optional[CategoryScheme] = None

    class Config:
        from_attributes = True
        populate_by_name = True


class PracticeReadSchema(BaseModel):
    id: int
    name: str
    description: str

    company: Optional[CompanyReadSchema] = None
    category: Optional[PracticeCategorySchema] = None

    class Config:
        from_attributes = True
        populate_by_name = True


class PracticeCreateSchema(BaseModel):
    name: str
    description: str
    category_id: Optional[int] = None

    class Config:
        from_attributes = True
        populate_by_name = True