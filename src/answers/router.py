from typing import List

from fastapi import APIRouter, Depends, status

# from src.auth import service, tokens
from src.auth.dependencies import valid_user_create, valid_refresh_token, valid_access_token
from src.auth.exceptions import InvalidToken
# from src.auth.schemas import UserRead, UserCreate, TokenPair, AuthUser, RefreshToken
from src.auth.service import CurrentUser
from src.database import AsyncDbSession

from src.answers import service
from src.answers.schemas import AnswerCreate, AnswerRead
from src.auth import service as auth_service

router = APIRouter()

@router.post("", response_model=AnswerRead)
async def create_answer(session: AsyncDbSession, answer_in: AnswerCreate, user: auth_service.CurrentUser):
    answer = await service.create_answer(session, answer_in, user.id)
    await session.commit()
    return answer


@router.get("", response_model=List[AnswerRead])
def get_answer(session: AsyncDbSession):
    answer = await service.create_answer(session)
    await session.commit()
    return answer


@router.put("")
def update_answer():
    pass


@router.delete("")
def delete_answer():
    pass