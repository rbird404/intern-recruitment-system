from typing import List

from fastapi import APIRouter

from src.auth import service
from src.database import AsyncDbSession
from src.grades import service
from src.grades.schemas import TestCreate, TestRead
from src.exceptions import BadRequest


router = APIRouter()


@router.post("", response_model=TestRead)
async def create_test(session: AsyncDbSession, test_in: TestCreate):
    test = await service.create_test(session, test_in)
    await session.commit()
    return test


@router.get("/{id}", response_model=TestRead)
async def get_test(session: AsyncDbSession, id: int):
    test = await service.get_test(session, id)
    if test is None:
        raise BadRequest
    return test


@router.get("", response_model=List[TestRead])
async def get_tests(session: AsyncDbSession):
    return await service.get_tests(session)


@router.delete("/{id}")
async def delete_test(session: AsyncDbSession, id: int):
    test = await service.delete_test(session, id)
    if test is None:
        raise BadRequest
    await session.commit()
    return test

