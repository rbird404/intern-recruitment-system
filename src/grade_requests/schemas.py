from pydantic import BaseModel, ConfigDict

from src.auth.schemas import UserRead
from src.grade_requests.enums import GradeRequestType, GradeUserType
from src.specializations.schemas import SpecializationRead


class GradeRequestCreate(BaseModel):
    specialization_id: int
    type: GradeUserType
    resume: str | None


class GradeRequestStatusUpdate(BaseModel):
    status: GradeRequestType


class TestList(BaseModel):
    tests: list[int]


class TestRead(BaseModel):
    id: int
    title: str
    description: str | None = None


class GradeRequestRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    resume: str | None
    specialization_id: int
    type: GradeUserType
    status: GradeRequestType
    tests: list[TestRead] = []
    user: UserRead


class GradeRequestReadFull(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    resume: str | None
    specialization: SpecializationRead
    type: GradeUserType
    status: GradeRequestType
    tests: list[TestRead] = []
    user: UserRead
    tech_lead: UserRead | None
    hr: UserRead | None


class Result(BaseModel):
    test_result: int | None
    grade_request_id: int
    test_id: int
