from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select
from src.answers.schemas import AnswerCreate

from src.answers.models import Answer
from src.code_execute.service import get_test_cases, run_test_case
from src.exceptions import BadRequest
from src.questions.models import Question


async def create_answer(session: AsyncSession, answer_in: AnswerCreate) -> Answer:
    question: Question = await session.scalar(
        select(Question).where(Question.id == answer_in.question_id)
    )
    if question is None:
        raise BadRequest

    coefficient = 0

    if question.type == "text":
        if question.text.content == answer_in.content:
            coefficient = 1
    else:
        code_id = question.code.id
        test_cases_result = []
        for test_case in await get_test_cases(session, code_id):
            result = await run_test_case(
                test_case,
                language=answer_in.language,
                code=answer_in.content
            )
            test_cases_result.append(result)

        len_ = len(test_cases_result)
        if len_ > 0:
            count_true = len([case_result for case_result in test_cases_result if case_result.status == 1])
            coefficient = count_true / len_

    answer = Answer(
        **answer_in.model_dump(),
        coefficient=coefficient
    )
    session.add(answer)
    return answer


async def get_answers(session: AsyncSession):
    answers = await session.scalars(
        select(Answer)
    )
    return answers


async def get_answer(session: AsyncSession, id_: int) -> Answer:
    answer = await session.scalar(
        select(Answer).where(Answer.id == id_)
    )
    return answer


async def remove_answer(session: AsyncSession, id_: int) -> Answer:
    answer = await session.scalar(
        delete(Answer).where(Answer.id == id_)
        .returning(Answer)
    )
    return answer
