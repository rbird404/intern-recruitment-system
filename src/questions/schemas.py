from pydantic import BaseModel, ConfigDict
from src.questions.utils import QuestionType


class TestCaseCreate(BaseModel):
    input: str | None = None
    output: str | None = None
    error: str | None = None


class CodeCreate(BaseModel):
    content: str
    test_cases: list[TestCaseCreate]


class TextCreate(BaseModel):
    content: str


class QuestionCreate(BaseModel):
    title: str
    description: str | None = None
    level: int
    type: QuestionType
    content: CodeCreate | TextCreate


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


class QuestionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str | None = None
    level: int
    type: QuestionType
    content: CodeRead | TextRead | None
