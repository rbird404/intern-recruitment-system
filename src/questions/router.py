from typing import List

from fastapi import APIRouter

from src.auth import service
from src.database import AsyncDbSession
from src.questions.models import Question
from src.questions.schemas import QuestionCreate, QuestionReadDetail, QuestionReadList
from src.questions import service
from src.exceptions import BadRequest
from src.database import remove_by_id

router = APIRouter()


@router.post("", response_model=QuestionReadDetail)
async def create_question(session: AsyncDbSession, question_in: QuestionCreate):
    question = await service.create_question(session, question_in)
    await session.refresh(question, ("text", "code"))
    await session.commit()
    return question


@router.get("", response_model=List[QuestionReadList])
async def get_questions(session: AsyncDbSession):
    questions = await service.get_questions_list(session)
    return questions


@router.get("/{id}", response_model=QuestionReadDetail)
async def get_question(session: AsyncDbSession, id: int):
    question = await service.get_question_by_id(session, id)
    if question is None:
        raise BadRequest
    return question


@router.delete("/{id}", response_model=QuestionReadList)
async def delete_question(session: AsyncDbSession, id: int):
    question = await remove_by_id(session, Question, id)
    if question is None:
        raise BadRequest
    await session.commit()
    return question
