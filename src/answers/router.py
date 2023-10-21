from typing import List

from fastapi import APIRouter
from src.database import AsyncDbSession

from src.answers import service
from src.answers.schemas import AnswerCreate, AnswerRead
from src.auth import service as auth_service
from src.exceptions import BadRequest

router = APIRouter()


@router.post("", response_model=AnswerRead)
async def create_answer(
        session: AsyncDbSession, answer_in: AnswerCreate, user: auth_service.CurrentUser
):
    answer = await service.create_answer(session, answer_in, user.id)
    await session.commit()
    return answer


@router.get("", response_model=List[AnswerRead])
async def get_answers(session: AsyncDbSession):
    answer = await service.get_answers(session)
    await session.commit()
    return answer


@router.get("/{id}")
async def get_answer(session: AsyncDbSession, id: int):
    answer = await service.get_answer(session, id)
    if answer is None:
        raise BadRequest
    return answer


@router.delete("/{id}")
async def delete_answer(session: AsyncDbSession, id: int):
    answer = await service.remove_answer(session, id)
    if answer is None:
        raise BadRequest
    await session.commit()
    return answer
