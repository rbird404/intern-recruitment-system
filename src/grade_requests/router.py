from fastapi import APIRouter, UploadFile

from src.auth import service
from src.auth.service import CurrentUser
from src.database import AsyncDbSession

from src.grade_requests import service
from src.grade_requests.schemas import GradeRequestStatusUpdate, TestList, GradeRequestRead

router = APIRouter()


@router.post("", status_code=200, response_model=GradeRequestRead)
async def user_create_grade_request(session: AsyncDbSession, user: CurrentUser, file_in: UploadFile = None):
    request = await service.create_user_grade_request(session, user.id, file_in)
    await session.commit()
    return request


@router.post("/{id}/tests", status_code=200, response_model=GradeRequestRead)
async def add_tests_in_grade_request(session: AsyncDbSession, id: int, tests: TestList):
    request = await service.add_test_in_grade_request(session, id, tests.tests)
    await session.commit()
    return request


@router.put("/{id}", status_code=200, response_model=GradeRequestRead)
async def change_status_grade_request(session: AsyncDbSession, id: int, status: GradeRequestStatusUpdate):
    request = await service.change_status(session, id, status)
    await session.commit()
    return request
