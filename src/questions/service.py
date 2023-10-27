from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload

from src.questions.models import Text, TestCase, Code, Question
from src.questions.schemas import TextCreate, TestCaseCreate, CodeCreate, QuestionCreate


async def create_text(session: AsyncSession, question_id: int, text_in: TextCreate):
    text = Text(question_id=question_id, content=text_in.content)
    session.add(text)
    return text


async def create_test_case(session: AsyncSession, code_id: int, test_case_in: TestCaseCreate):
    test_case = TestCase(code_id=code_id, **test_case_in.model_dump())
    session.add(test_case)
    return test_case


async def create_code(session: AsyncSession, question_id: int, code_in: CodeCreate):
    code = Code(
        question_id=question_id,
        **code_in.model_dump(exclude={"test_cases"})
    )
    session.add(code)
    await session.flush()
    test_cases = code_in.test_cases
    for test_case_in in test_cases:
        await create_test_case(session, code.id, test_case_in)

    return code


async def create_question(session: AsyncSession, question_in: QuestionCreate):
    question = Question(
        **question_in.model_dump(exclude={'content'})
    )
    session.add(question)
    await session.flush()
    type_ = question_in.type

    if type_ == "text":
        await create_text(session, question.id, question_in.content)
    elif type_ == "code":
        await create_code(session, question.id, question_in.content)

    return question


async def get_question_by_id(session: AsyncSession, id_: int) -> Question:
    question = await session.scalar(
        select(Question).where(Question.id == id_)
    )
    return question


async def get_questions_list(session: AsyncSession):
    questions = await session.scalars(
        select(Question).options(
            noload(Question.text),
            noload(Question.code)
        )
    )
    return questions
