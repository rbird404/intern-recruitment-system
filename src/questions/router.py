from typing import List

from fastapi import APIRouter
from src.auth import service
from src.database import AsyncDbSession
from .schemas import QuestionCreate, QuestionRead
from src.questions import service
from src.exceptions import BadRequest
router = APIRouter()


@router.post("", response_model=QuestionRead)
async def create_question(session: AsyncDbSession, question_in: QuestionCreate):
    question = await service.create_question(session, question_in)
    await session.commit()
    return service.serialize_question(question)


@router.get("", response_model=List[QuestionRead])
async def get_questions(session: AsyncDbSession):
    questions = await service.get_questions(session)
    return [
        service.serialize_question(question)
        for question in questions
    ]


@router.get("/{id}", response_model=QuestionRead)
async def get_question(session: AsyncDbSession, id: int):
    question = await service.get_question(session, id)
    if question is None:
        raise BadRequest
    return service.serialize_question(question)


@router.delete("/{id}")
async def delete_question(session: AsyncDbSession, id: int):
    question = await service.remove_question(session, id)
    if question is None:
        raise BadRequest
    await session.commit()
    return dict(question.__dict__)
