from pydantic import BaseModel
from src.questions.schemas import QuestionCreate, QuestionRead


class QuestionCreateOrUpdate(QuestionCreate):
    id: int | None = None


class TestQuestionCreate(BaseModel):
    point: int
    question: QuestionCreateOrUpdate


class TestCreate(BaseModel):
    title: str
    description: str | None = None
    questions: list[TestQuestionCreate]


class TestQuestionRead(BaseModel):
    id: int
    point: int
    question: QuestionRead


class TestRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    questions: list[TestQuestionRead]
