from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload

from .models import Test, TestQuestion
from .schemas import TestCreate


async def create_test(session: AsyncSession, test_in: TestCreate):
    test = Test(**test_in.model_dump(exclude={"questions"}))
    session.add(test)
    await session.flush()

    for question_in in test_in.questions:
        session.add(
            TestQuestion(
                test_id=test.id,
                question_id=question_in.question_id,
                point=question_in.point
            )
        )
    return test


async def get_test_by_id(session: AsyncSession, id_: int):
    test = await session.scalar(
        select(Test).where(Test.id == id_)
    )
    return test


async def get_tests(session: AsyncSession):
    tests = await session.scalars(
        select(Test).options(
            noload(Test.questions)
        )
    )
    return tests
