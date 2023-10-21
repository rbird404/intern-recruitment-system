from pydantic import BaseModel, ConfigDict

from src.answers.utils import AnswerType


class AnswerCreate(BaseModel):
    coefficient: float
    question_id: int
    type: AnswerType


class AnswerRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    coefficient: float
    question_id: int
    type: AnswerType
