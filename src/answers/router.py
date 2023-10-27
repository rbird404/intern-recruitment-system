from typing import List
from fastapi import APIRouter

from src.database import AsyncDbSession, remove_by_id
from src.answers.models import Answer
from src.answers import service
from src.answers.schemas import AnswerCreate, AnswerRead
from src.exceptions import BadRequest

router = APIRouter()


@router.post("", response_model=List[AnswerRead])
async def create_answers(
        session: AsyncDbSession, answers_in: List[AnswerCreate]
):
    answers = []
    for answer in answers_in:
        answers.append(
            await service.create_answer(session, answer)
        )
    await session.commit()
    return answers


@router.get("", response_model=List[AnswerRead])
async def get_answers(session: AsyncDbSession):
    answer = await service.get_answers(session)
    return answer


@router.get("/{id}")
async def get_answer(session: AsyncDbSession, id: int):
    answer = await service.get_answer(session, id)
    if answer is None:
        raise BadRequest
    return answer


@router.delete("/{id}")
async def delete_answer(session: AsyncDbSession, id: int):
    answer = await remove_by_id(session, Answer, id)
    if answer is None:
        raise BadRequest
    await session.commit()
    return answer
