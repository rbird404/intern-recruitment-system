from typing import List

from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import (
    String,
    ForeignKey,
    Integer, Enum
)

from src.auth.models import User
from src.database import Base
from src.grade_requests.utils import GradeRequestType
from src.grades.models import Test


class GradeRequest(Base):
    __tablename__ = "grade_requests"
    user_id = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    status = mapped_column(Enum(GradeRequestType), default=GradeRequestType.entering)
    resume = mapped_column(String, nullable=True)
    tests: Mapped[List[Test]] = relationship(lazy='selectin', secondary="grade_request_tests")
    user: Mapped[User] = relationship(lazy='selectin')


class GradeRequestTests(Base):
    __tablename__ = "grade_request_tests"

    grade_request_id = mapped_column(Integer, ForeignKey("grade_requests.id", ondelete="SET NULL"), nullable=True)
    test_id = mapped_column(Integer, ForeignKey("tests.id", ondelete="SET NULL"), nullable=True)
