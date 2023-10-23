from typing import Annotated, Type
from fastapi import Depends
from sqlalchemy import delete

from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from sqlalchemy.ext.asyncio import (
    async_sessionmaker, create_async_engine, AsyncSession
)

from src.config import settings

__all__ = ("Base", "DATABASE_URL", "AsyncDbSession", "remove_by_id")

DATABASE_URL = str(settings.DATABASE_URL)

engine = create_async_engine(
    DATABASE_URL,
    echo=False
)

async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.close()


AsyncDbSession = Annotated[AsyncSession, Depends(get_async_session)]


class Base(DeclarativeBase):
    ...


async def remove_by_id(session: AsyncSession, model: Type[Base], id_: int) -> Base:
    obj = await session.scalar(
        delete(model).where(model.id == id_)
        .returning(model)
    )
    return obj
