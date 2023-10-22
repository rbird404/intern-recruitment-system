from pydantic import BaseModel, ConfigDict

from src.answers.utils import AnswerType


class AnswerCreate(BaseModel):
    grade_request_id: int
    test_id: int
    question_id: int
    content: str | None = None
    language: str | None = None


class AnswerRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    coefficient: float = 0.0
    grade_request_id: int
    test_id: int
    question_id: int
    language: str | None = None
    content: str | None = None
