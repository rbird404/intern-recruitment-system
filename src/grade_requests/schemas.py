from pydantic import BaseModel, ConfigDict

from src.grade_requests.utils import GradeRequestType


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
    status: GradeRequestType
    tests: list[TestRead] = []
    user: UserRead
