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

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    point = mapped_column(Integer, nullable=False)

    # relationships
    test_id = mapped_column(Integer, ForeignKey("tests.id", ondelete="CASCADE"), primary_key=True)
    question_id = mapped_column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), primary_key=True)
    question: Mapped[Question] = relationship(lazy="joined")


class Test(Base):
    __tablename__ = "tests"

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    title = mapped_column(String, nullable=False)
    description = mapped_column(String)

    # relationships
    creator_id = mapped_column(Integer, ForeignKey("users.id"))
    questions: Mapped[List[TestQuestion]] = relationship(lazy="joined")
