from sqlalchemy.orm import mapped_column
from sqlalchemy import (
    String,
    ForeignKey,
    Enum,
    Integer,
    Float
)

from src.database import Base
import enum


from src.grades import QuestionType


class Ansswer(Base):
    __tablename__ = "answers"
    
    user_id = mapped_column(Integer, ForeignKey("users.id"))
    coefficient = mapped_column(Float, nullable=False)
    test_id = mapped_column(Integer, ForeignKey("tests.id"))
    question_id = mapped_column(Integer, ForeignKey("questions.id"))
    type = mapped_column(Enum(QuestionType), nullable=False)
    
    