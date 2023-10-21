from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select
from src.answers.schemas import AnswerCreate

from src.answers.models import Answer


async def create_answer(session: AsyncSession, answer_id: AnswerCreate, user_id: int) -> Answer:
    answer = Answer(
        user_id=user_id,
        **answer_id.model_dump()
    )
    session.add(answer)
    return answer


async def get_answers(session: AsyncSession):
    answers = await session.scalars(
        select(Answer)
    )
    return answers


async def get_answer(session: AsyncSession, id_: int) -> Answer:
    answer = await session.scalar(
        select(Answer).where(Answer.id == id_)
    )
    return answer


async def remove_answer(session: AsyncSession, id_: int) -> Answer:
    answer = await session.scalar(
        delete(Answer).where(Answer.id == id_)
        .returning(Answer)
    )
    return answer
