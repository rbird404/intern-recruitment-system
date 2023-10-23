from sqlalchemy.orm import mapped_column
from sqlalchemy import (
    String,
    Integer
)

from src.database import Base


class Specialization(Base):
    __tablename__ = 'specializations'

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    name = mapped_column(String, nullable=False)
    description = mapped_column(String)
