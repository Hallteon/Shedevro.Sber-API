from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas, FastAPIUsers
from api.utils.auth_misc import *
from models.practice_models import Student, Company, Provider
from settings import config_parameters


class StudentManager(IntegerIDMixin, BaseUserManager[Student, int]):
    reset_password_token_secret = config_parameters.AUTH_SECRET
    verification_token_secret = config_parameters.AUTH_SECRET

    async def on_after_register(self, user, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)

        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


class CompanyManager(IntegerIDMixin, BaseUserManager[Company, int]):
    reset_password_token_secret = config_parameters.AUTH_SECRET
    verification_token_secret = config_parameters.AUTH_SECRET

    async def on_after_register(self, user, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)

        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


class ProviderManager(IntegerIDMixin, BaseUserManager[Provider, int]):
    reset_password_token_secret = config_parameters.AUTH_SECRET
    verification_token_secret = config_parameters.AUTH_SECRET

    async def on_after_register(self, user, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)

        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_student_manager(user_db=Depends(get_student_db)):
    yield StudentManager(user_db)

async def get_company_manager(user_db=Depends(get_company_db)):
    yield CompanyManager(user_db)

async def get_provider_manager(user_db=Depends(get_provider_db)):
    yield ProviderManager(user_db)
