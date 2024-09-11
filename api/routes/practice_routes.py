from typing import List

from fastapi import status
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_async_session
from api.schemas.practice_schemas import PracticeReadSchema, PracticeCreateSchema
from auth_setup import (auth_backend, fastapi_users_students, fastapi_users_companies,
                        fastapi_users_providers)

from models.practice_models import Company, Practice


router = APIRouter(prefix='/practice',
                   tags=['Practice'])


@router.post('/create')
async def create_practice(practice: PracticeCreateSchema,
                          session: AsyncSession = Depends(get_async_session),
                          company: Company = Depends(fastapi_users_companies.current_user())):
    practice_obj = Practice(name=practice.name, description=practice.description,
                       category_id=practice.category_id, company_id=company.id)

    session.add(practice_obj)
    await session.commit()

    return practice_obj


@router.get('/get/{practice_id}', response_model=PracticeReadSchema)
async def read_practice(practice_id: int, session: AsyncSession = Depends(get_async_session)):
    practice_query = await session.execute(select(Practice).filter(Practice.id == practice_id))
    practice = practice_query.scalars().first()

    if practice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Practice not found!')

    return practice


@router.get('/get_all', response_model=List[PracticeReadSchema])
async def read_practices(session: AsyncSession = Depends(get_async_session)):
    practice_query = await session.execute(select(Practice))
    practices = practice_query.scalars().all()

    return practices


@router.put('/get/{practice_id}', response_model=PracticeReadSchema)
async def get_practice(practice_id: int, practice_update: PracticeCreateSchema,
                      session: AsyncSession = Depends(get_async_session)):
    practice_query = await session.execute(select(Practice).filter(Practice.id == practice_id))
    practice = practice_query.scalars().first()

    if practice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='')

    for field, value in practice_update.dict(exclude_unset=True).items():
        setattr(practice, field, value)

    await session.commit()

    return practice


@router.delete('/delete/{practice_id}', response_model=dict)
async def delete_practice(practice_id: int, session: AsyncSession = Depends(get_async_session)):
    practice_query = await session.execute(select(Practice).filter(Practice.id == practice_id))
    practice = practice_query.scalars().first()

    if practice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Practice not found!')

    await session.delete(practice)
    await session.commit()

    return {'message': 'Practice deleted successfully!'}