from fastapi import APIRouter, Depends, status

from src.auth import service, tokens
from src.auth.dependencies import valid_user_create, valid_refresh_token, valid_access_token
from src.auth.exceptions import InvalidToken
from src.auth.schemas import UserRead, UserCreate, TokenPair, AuthUser, RefreshToken
from src.auth.service import CurrentUser
from src.database import AsyncDbSession

from src.questions import service
from src.answers.utils import AnswerCreate

router = APIRouter()

@router.post("")
async def create_answer(session: AsyncDbSession, question_in: AnswerCreate):
    question = await service.create_question(session, question_in)
    await session.commit()
    return question.id


@router.get("")
def create_answer():
    pass


@router.put("")
def update_answer():
    pass


@router.delete("")
def delete_answer():
    pass