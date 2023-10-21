from pydantic import BaseModel, ConfigDict

from src.questions.utils import QuestionType

class AnswerCreate(BaseModel):
    coefficient: float
    question_id :int 
    test_cases_id: int
    type: QuestionType
    
class AnswerRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    coefficient: float
    question_id :int 
    test_cases_id: int
    type: QuestionType
    
