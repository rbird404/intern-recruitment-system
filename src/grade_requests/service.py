import uuid

import aiofiles
from fastapi import UploadFile
from sqlalchemy import delete, select, update

from src.config import STATIC_DIR
from src.database import AsyncDbSession
from src.grades.models import Test
from .models import GradeRequest, GradeRequestTests
from .schemas import GradeRequestStatusUpdate


async def create_user_grade_request(session: AsyncDbSession, user_id, file_in: UploadFile = None):
    chunk_size = 1024 * 1024 * 50
    resume = None
    if file_in is not None:
        async with aiofiles.open(
                str(STATIC_DIR / f"{uuid.uuid4()}.pdf"),
                "wb"
        ) as file:
            while chunk := await file_in.read(chunk_size):
                await file.write(chunk)
        resume = file.name
    request = GradeRequest(user_id=user_id, resume=resume)
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
