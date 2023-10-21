from pydantic import BaseModel, ConfigDict, Field

from src.grade_requests.utils import GradeRequestType, GradeUserType


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


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int


class GradeRequestRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    resume: str | None
    specialization_id: int
    type: GradeUserType
    status: GradeRequestType
    tests: list[TestRead] = []
    user: UserRead
