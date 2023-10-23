from typing import List
from fastapi import APIRouter

from src.database import AsyncDbSession
from src.specializations import service
from src.specializations.models import Specialization
from src.specializations.schemas import SpecializationCreate, SpecializationRead
from src.exceptions import BadRequest
from src.database import remove_by_id

router = APIRouter()


@router.post("", response_model=SpecializationRead)
async def create_specialization(
        session: AsyncDbSession, specialization_in: SpecializationCreate
):
    answer = await service.create_specialization(session, specialization_in)
    await session.commit()
    return answer


@router.get("", response_model=List[SpecializationRead])
async def get_specializations(session: AsyncDbSession):
    return await service.get_specializations_list(session)


@router.get("/{id}", response_model=SpecializationRead)
async def get_specialization(session: AsyncDbSession, id: int):
    specialization = await service.get_specialization(session, id)
    if specialization is None:
        raise BadRequest
    return specialization


@router.delete("/{id}", response_model=SpecializationRead)
async def delete_specialization(session: AsyncDbSession, id: int):
    specialization = await remove_by_id(session, Specialization, id)
    if specialization is None:
        raise BadRequest
    await session.commit()
    return specialization
