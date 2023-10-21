from pydantic import BaseModel

from src.questions.utils import QuestionType

class AnswerCreate(BaseModel):
    coefficient: float
    test_id : int 
    question_id: int
    type: QuestionType