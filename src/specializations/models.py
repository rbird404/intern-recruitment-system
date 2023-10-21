from typing import Any, List
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import (
    String,
    ForeignKey,
    Integer
)

from src.database import Base


class Specialization(Base):
    __tablename__ = 'specializations'
    name = mapped_column(String, nullable=False)
    description = mapped_column(String)
