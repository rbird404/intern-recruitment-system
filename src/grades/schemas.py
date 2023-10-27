from pydantic import BaseModel

from src.questions.schemas import QuestionReadDetail


class TestQuestionCreate(BaseModel):
    point: int
    question_id: int


class TestCreate(BaseModel):
    title: str
    description: str | None = None
    questions: list[TestQuestionCreate] = []


class TestQuestionRead(BaseModel):
    point: int
    question: QuestionReadDetail


class TestRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    questions: list[TestQuestionRead] = []
