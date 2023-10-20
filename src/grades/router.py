from fastapi import APIRouter, Depends, status

from src.auth import service, tokens
from src.auth.dependencies import valid_user_create, valid_refresh_token, valid_access_token
from src.auth.exceptions import InvalidToken
from src.auth.schemas import UserRead, UserCreate, TokenPair, AuthUser, RefreshToken
from src.auth.service import CurrentUser
from src.database import AsyncDbSession

router = APIRouter(
    prefix="questions"
)


@router.post("")
def create_question():
    pass


@router.get("")
def create_question():
    pass

@router.put("")
def update_question():
    pass

@router.delete("")
def delete_question():
    pass

