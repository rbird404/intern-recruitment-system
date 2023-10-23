from sqlalchemy.orm import mapped_column
from sqlalchemy import (
    ForeignKey,
    Enum,
    Integer,
    Float, String
)

from src.answers.utils import AnswerType
from src.database import Base


class Answer(Base):
    __tablename__ = "answers"
    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    coefficient = mapped_column(Float, nullable=False)
    content = mapped_column(String, nullable=True)
    language = mapped_column(String, nullable=True)

    # relationships
    test_id = mapped_column(Integer, ForeignKey("tests.id", ondelete="CASCADE"))
    grade_request_id = mapped_column(Integer, ForeignKey("grade_requests.id", ondelete="CASCADE"))
    question_id = mapped_column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))
