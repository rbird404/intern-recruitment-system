from pydantic import BaseModel, ConfigDict

from src.questions.enums import QuestionType


class TestCaseCreate(BaseModel):
    input: str | None = None
    output: str | None = None
    error: str | None = None


class CodeCreate(BaseModel):
    content: str
    test_cases: list[TestCaseCreate]


class TextCreate(BaseModel):
    content: str


class TestCaseRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    input: str | None = None
    output: str | None = None
    error: str | None = None


class CodeRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    content: str
    test_cases: list[TestCaseRead]


class TextRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    content: str


class QuestionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    description: str | None = None
    level: int
    type: QuestionType


class QuestionReadDetail(QuestionBase):
    id: int
    content: CodeRead | TextRead | None


class QuestionReadList(QuestionBase):
    id: int


class QuestionCreate(QuestionBase):
    content: CodeCreate | TextCreate
