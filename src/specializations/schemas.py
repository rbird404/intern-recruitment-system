from pydantic import BaseModel, ConfigDict

from src.answers.utils import AnswerType


class SpecializationCreate(BaseModel):
    name: str
    description: str | None = None


class SpecializationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str | None = None
