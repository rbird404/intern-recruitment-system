from typing import List

from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import (
    String,
    ForeignKey,
    Integer, Enum
)

from src.auth.models import User
from src.database import Base
from src.grade_requests.utils import GradeRequestType, GradeUserType
from src.grades.models import Test
from src.specializations.models import Specialization


class GradeRequest(Base):
    __tablename__ = "grade_requests"

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    status = mapped_column(Enum(GradeRequestType), default=GradeRequestType.entering)
    type = mapped_column(Enum(GradeUserType), default=GradeUserType.intern)
    resume = mapped_column(String, nullable=True)

    # relationships
    tests: Mapped[List[Test]] = relationship(secondary="grade_request_tests")

    specialization_id = mapped_column(Integer, ForeignKey("specializations.id", ondelete="SET NULL"), nullable=True)
    specialization: Mapped[Specialization] = relationship()

    user_id = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    user: Mapped[User] = relationship(foreign_keys=[user_id])

    hr_id = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    hr: Mapped[User] = relationship(foreign_keys=[hr_id])

    tech_lead_id = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    tech_lead: Mapped[User] = relationship(foreign_keys=[tech_lead_id])


class GradeRequestTests(Base):
    __tablename__ = "grade_request_tests"

    grade_request_id = mapped_column(
        Integer,
        ForeignKey("grade_requests.id", ondelete="CASCADE"),
        nullable=True,
        primary_key=True
    )
    test_id = mapped_column(
        Integer,
        ForeignKey("tests.id", ondelete="CASCADE"),
        nullable=True,
        primary_key=True
    )


class TestResult(Base):
    __tablename__ = "test_results"

    grade_request_id = mapped_column(Integer, primary_key=True)
    test_id = mapped_column(Integer, primary_key=True)
    result = mapped_column(Integer)


# SQL test_result
# create view test_results as select sum(foo.answer_result) / sum(foo.question_point) * 100 as result, foo.grade_request_id, foo.test_id from (select tq.test_id, tq.question_id, a.grade_request_id, max(point) as question_point, max(a.coefficient) * max(tq.point) as answer_result from test_questions tq join answers a on tq.test_id = a.test_id and tq.question_id = a.question_id
# group by tq.test_id, tq.question_id, a.grade_request_id) as foo group by foo.grade_request_id, foo.test_id
