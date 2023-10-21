from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Test, TestQuestion
from .schemas import TestCreate
from src.questions import service as question_service


async def create_test(session: AsyncSession, test_in: TestCreate):
    test = Test(**test_in.model_dump(exclude={"questions"}))
    session.add(test)
    await session.flush()

    for question_test in test_in.questions:
        question_in = question_test.question
        point = question_test.point
        if question_in.id is None:
            question = await question_service.create_question(session, question_in)
            session.add(question)
            await session.flush()
        else:
            question = await question_service.get_question(session, question_in.id)
            if question is None:
                continue

        session.add(
            TestQuestion(test_id=test.id, question_id=question.id, point=point)
        )

    await session.refresh(test)
    return test


async def get_test(session: AsyncSession, id_: int):
    test = await session.scalar(
        select(Test).where(Test.id == id_)
    )
    return test


async def get_tests(session: AsyncSession):
    test = await session.scalars(
        select(Test)
    )
    return test


async def delete_test(session: AsyncSession, id_: int):
    test = await session.scalar(
        delete(Test).where(Test.id == id_)
        .returning(Test)
    )
    return test
