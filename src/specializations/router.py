from typing import List

from fastapi import APIRouter
from src.database import AsyncDbSession

from src.specializations import service
from src.specializations.schemas import SpecializationCreate, SpecializationRead
from src.auth import service as auth_service
from src.exceptions import BadRequest

router = APIRouter()


@router.post("", response_model=SpecializationRead)
async def create_specialization(
        session: AsyncDbSession, specialization_in: SpecializationCreate, user: auth_service.CurrentUser
):
    answer = await service.create_specialization(session, specialization_in)
    await session.commit()
    return answer


@router.get("", response_model=List[SpecializationRead])
async def get_specializations(session: AsyncDbSession):
    specializations = await service.get_specializations(session)
    return specializations


@router.get("/{id}")
async def get_specialization(session: AsyncDbSession, id: int):
    specialization = await service.get_specialization(session, id)
    if specialization is None:
        raise BadRequest
    return specialization


@router.delete("/{id}")
async def delete_specialization(session: AsyncDbSession, id: int):
    specialization = await service.remove_specialization(session, id)
    if specialization is None:
        raise BadRequest
    await session.commit()
    return specialization
