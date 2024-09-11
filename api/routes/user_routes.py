import os
import uuid
from sys import prefix

from fastapi import APIRouter, UploadFile, BackgroundTasks, Form, File, HTTPException
from fastapi.params import Depends
from auth_setup import (auth_backend, fastapi_users_students, fastapi_users_companies,
                        fastapi_users_providers)
from api.schemas.user_schemas import *

from models.practice_models import Student, Provider, Company
from settings import config_parameters


router = APIRouter(prefix='/users',
                   tags=['Users'])


# Students Auth

router.include_router(
    fastapi_users_students.get_auth_router(auth_backend),
    prefix='/students',
)

router.include_router(
    fastapi_users_students.get_register_router(StudentAuthReadSchema, StudentCreateSchema),
    prefix='/students',
)

# Company Auth

router.include_router(
    fastapi_users_companies.get_auth_router(auth_backend),
    prefix='/companies',
)

router.include_router(
    fastapi_users_companies.get_register_router(CompanyAuthReadSchema, CompanyCreateSchema),
    prefix='/companies',
)

# Provider Auth

router.include_router(
    fastapi_users_providers.get_auth_router(auth_backend),
    prefix='/providers',
)

router.include_router(
    fastapi_users_providers.get_register_router(ProviderAuthReadSchema, ProviderCreateSchema),
    prefix='/providers'
)


# Auth Routes

@router.get('/students/me', response_model=StudentReadSchema)
async def get_me_student(user: Student = Depends(fastapi_users_students.current_user())):
    return user

@router.get('/companies/me', response_model=CompanyReadSchema)
async def get_me_company(user: CompanyReadSchema = Depends(fastapi_users_companies.current_user())):
    return user

@router.get('/providers/me', response_model=ProviderReadSchema)
async def get_me_provider(user: Provider = Depends(fastapi_users_providers.current_user())):
    return user
