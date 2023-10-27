from pydantic import BaseModel, ConfigDict


class AnswerBase(BaseModel):
    grade_request_id: int
    test_id: int
    question_id: int
    content: str | None = None
    language: str | None = None


class AnswerCreate(AnswerBase):
    ...


class AnswerRead(AnswerBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    coefficient: float = 0.0

