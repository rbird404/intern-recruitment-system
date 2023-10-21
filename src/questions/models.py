from sqlalchemy.orm import mapped_column
from sqlalchemy import (
    String,
    ForeignKey,
    Enum, Integer
)

from src.database import Base
from src.questions.utils import QuestionType
from sqlalchemy.orm import relationship


class TestCase(Base):
    __tablename__ = 'test_cases'
    input = mapped_column(String, nullable=True)
    output = mapped_column(String, nullable=True)
    error = mapped_column(String, nullable=True)
    code_id = mapped_column(ForeignKey("codes.id", ondelete="CASCADE"))


class Code(Base):
    __tablename__ = "codes"
    content = mapped_column(String, nullable=False)
    question_id = mapped_column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))
    test_cases = relationship(TestCase, lazy='selectin', uselist=True)


class Text(Base):
    __tablename__ = 'texts'
    content = mapped_column(String, nullable=False)
    question_id = mapped_column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))


class Question(Base):
    __tablename__ = "questions"
    title = mapped_column(String, nullable=False)
    description = mapped_column(String)
    level = mapped_column(Integer, nullable=False)
    type = mapped_column(Enum(QuestionType), nullable=False)
    code = relationship(Code, lazy='selectin', uselist=False)
    text = relationship(Text, lazy='selectin', uselist=False)
