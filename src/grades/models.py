from sqlalchemy.orm import mapped_column
from sqlalchemy import (
    String,
    ForeignKey,
    Enum,
    Integer
)

from src.database import Base
import enum


class QuestionType(enum.Enum):
    text = "text"
    code = "code"


class Test(Base):
    __tablename__ = "tests"

    title = mapped_column(String, nullable=False)
    description = mapped_column(String)
    type = mapped_column(Enum(QuestionType), nullable=False)
    creator_id = mapped_column(Integer, ForeignKey("users.id"))


class TestQuestion(Base):
    __tablename__ = "test_questions"
    test_id = mapped_column(Integer, ForeignKey("tests.id"))
    question_id = mapped_column(Integer, ForeignKey("questions.id"))
