from sqlalchemy.orm import mapped_column
from sqlalchemy import (
    ForeignKey,
    Enum,
    Integer,
    Float
)

from src.answers.utils import AnswerType
from src.database import Base


class Answer(Base):
    __tablename__ = "answers"

    user_id = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    coefficient = mapped_column(Float, nullable=False)
    test_id = mapped_column(Integer, ForeignKey("tests.id", ondelete="CASCADE"))
    question_id = mapped_column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))
    type = mapped_column(Enum(AnswerType), nullable=False)
