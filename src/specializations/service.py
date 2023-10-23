from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select
from src.specializations.schemas import SpecializationBase
from .models import Specialization


async def create_specialization(session: AsyncSession, specialization_id: SpecializationBase) -> Specialization:
    specialization = Specialization(
        **specialization_id.model_dump()
    )
    session.add(specialization)
    return specialization


async def get_specializations_list(session: AsyncSession):
    specializations = await session.scalars(
        select(Specialization)
    )
    return specializations


async def get_specialization(session: AsyncSession, id_: int) -> Specialization:
    specialization = await session.scalar(
        select(Specialization).where(Specialization.id == id_)
    )
    return specialization


async def remove_specialization(session: AsyncSession, id_: int) -> Specialization:
    specialization = await session.scalar(
        delete(Specialization).where(Specialization.id == id_)
        .returning(Specialization)
    )
    return specialization
