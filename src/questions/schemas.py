from pydantic import BaseModel

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
