from typing import List

from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import (
    String,
    ForeignKey,
    Integer
)

from src.database import Base
from src.questions.models import Question


class TestQuestion(Base):
    __tablename__ = "test_questions"
    test_id = mapped_column(Integer, ForeignKey("tests.id", ondelete="CASCADE"), primary_key=True)
    question_id = mapped_column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), primary_key=True)
    point = mapped_column(Integer, nullable=False)
    question: Mapped[Question] = relationship(lazy="selectin")


class Test(Base):
    __tablename__ = "tests"

    title = mapped_column(String, nullable=False)
    description = mapped_column(String)
    creator_id = mapped_column(Integer, ForeignKey("users.id"))
    questions: Mapped[List[TestQuestion]] = relationship(lazy="selectin")
