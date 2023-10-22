import logging
from typing import List

from fastapi import APIRouter, UploadFile

from src.auth import service
from src.auth.service import CurrentUser
from src.database import AsyncDbSession
from src.exceptions import BadRequest

from src.grade_requests import service
from src.grade_requests.schemas import GradeRequestStatusUpdate, TestList, GradeRequestRead, GradeRequestCreate, \
    GradeRequestReadFull

router = APIRouter()


@router.post("", status_code=200, response_model=GradeRequestRead)
async def user_create_grade_request(
        session: AsyncDbSession,
        user: CurrentUser,
        grade_request_in: GradeRequestCreate
):
    request = await service.create_user_grade_request(session, user.id, grade_request_in)
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


@router.put("/{request_id}/tech_lead/{user_id}", response_model=GradeRequestReadFull)
async def add_tech_lead_in_grade_requests(
        session: AsyncDbSession, request_id: int, user_id: int
):
    request = await service.add_user(session, request_id, user_id, "tech_lead")
    if request is None:
        raise BadRequest
    await session.commit()
    return request


@router.put("/{request_id}/hr/{user_id}", response_model=GradeRequestReadFull)
async def add_tech_lead_in_grade_requests(
        session: AsyncDbSession, request_id: int, user_id: int
):
    request = await service.add_user(session, request_id, user_id, "hr")
    if request is None:
        raise BadRequest
    await session.commit()
    return request


@router.post("/load")
async def load_file(file_in: UploadFile):
    return await service.load_file(file_in)


@router.get("", response_model=List[GradeRequestReadFull])
async def get_grades(session: AsyncDbSession, user: CurrentUser):
    candidate_id = None
    if user.role == "Candidate":
        candidate_id = user.id
    return await service.get_grade_requests(session, candidate_id)
