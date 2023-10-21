import uuid

import aiofiles
from fastapi import UploadFile
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import STATIC_DIR
from src.database import AsyncDbSession
from src.grades.models import Test
from .models import GradeRequest, GradeRequestTests
from .schemas import GradeRequestStatusUpdate, GradeRequestCreate
from ..exceptions import BadRequest


async def create_user_grade_request(
        session: AsyncDbSession,
        user_id: int,
        grade_request_in: GradeRequestCreate,
):
    request = GradeRequest(
        user_id=user_id,
        **grade_request_in.model_dump()
    )
    session.add(request)
    await session.flush()
    await session.refresh(request)
    return request


async def add_test_in_grade_request(session: AsyncDbSession, grade_request_id, tests: list[int]):
    await session.execute(
        delete(GradeRequestTests).where(GradeRequestTests.id == grade_request_id)
    )
    tests = await session.scalars(
        select(Test.id).where(Test.id.in_(tests))
    )
    for test_id in tests:
        session.add(
            GradeRequestTests(grade_request_id=grade_request_id, test_id=test_id)
        )
    request = await session.scalar(
        select(GradeRequest).where(GradeRequest.id == grade_request_id)
    )
    return request


async def change_status(session: AsyncDbSession, grade_request_id, status: GradeRequestStatusUpdate):
    request = await session.scalar(
        update(GradeRequest)
        .values({"status": status.status})
        .where(GradeRequest.id == grade_request_id)
        .returning(GradeRequest)
    )
    return request


async def get_grade_requests(session: AsyncDbSession):
    requests = await session.scalars(
        select(GradeRequest)
    )
    return requests


async def load_file(file_in) -> str:
    chunk_size = 1024 * 1024 * 50
    async with aiofiles.open(
            str(STATIC_DIR / f"{uuid.uuid4()}.pdf"),
            "wb"
    ) as file:
        while chunk := await file_in.read(chunk_size):
            await file.write(chunk)
    return file.name


async def add_user(session: AsyncSession, request_id: int, user_id: int, role: str):
    data = dict()
    if role == "tech_lead":
        data["tech_lead_id"] = user_id
    else:
        data["hr_id"] = user_id

    request = await session.scalar(
        update(GradeRequest)
        .values(**data).where(GradeRequest.id == request_id)
        .returning(GradeRequest)
    )
    return request
