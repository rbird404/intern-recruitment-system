
from sqlalchemy.ext.asyncio import AsyncSession

from src.questions.models import Text, TestCase, Code, Question
from src.questions.schemas import TextCreate, TestCaseCreate, CodeCreate, QuestionCreate
from src.answers.models import Answer
from src.answers.schemas import AnswerCreate

from src.answers.models import Answer


async def create_answer(session: AsyncSession, answer_id:AnswerCreate , user_id: int):
    answer = Answer(
        user_id = user_id,
        **answer_id.model_dump()
    )
    session.add(answer)
    return answer

