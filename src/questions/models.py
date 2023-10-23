from sqlalchemy.orm import mapped_column
from sqlalchemy import (
    String,
    ForeignKey,
    Enum,
    Integer
)

from src.database import Base
from src.questions.enums import QuestionType
from sqlalchemy.orm import relationship

from sqlalchemy.orm.attributes import InstrumentedAttribute


class TestCase(Base):
    __tablename__ = 'test_cases'

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    input = mapped_column(String, nullable=True)
    output = mapped_column(String, nullable=True)
    error = mapped_column(String, nullable=True)

    # relationships
    code_id = mapped_column(ForeignKey("codes.id", ondelete="CASCADE"))


class Code(Base):
    __tablename__ = "codes"

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    content = mapped_column(String, nullable=False)

    # relationships
    question_id = mapped_column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))
    test_cases = relationship(TestCase, lazy='selectin', uselist=True)


class Text(Base):
    __tablename__ = 'texts'

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    content = mapped_column(String, nullable=False)

    # relationships
    question_id = mapped_column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))


class Question(Base):
    __tablename__ = "questions"

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    title = mapped_column(String, nullable=False)
    description = mapped_column(String)
    level = mapped_column(Integer, nullable=False)
    type = mapped_column(Enum(QuestionType), nullable=False)

    # relationships
    code = relationship(Code, uselist=False)
    text = relationship(Text, uselist=False)

    @property
    def content(self) -> InstrumentedAttribute:
        if self.code:
            return self.code
        return self.text
