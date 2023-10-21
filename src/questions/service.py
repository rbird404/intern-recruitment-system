import logging

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.questions.models import Text, TestCase, Code, Question
from src.questions.schemas import TextCreate, TestCaseCreate, CodeCreate, QuestionCreate, QuestionRead


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
    await session.refresh(question)
    return question


async def remove_question(session: AsyncSession, id_: int) -> Question:
    question = await session.scalar(
        delete(Question).where(Question.id == id_)
        .returning(Question)
    )
    return question


async def get_question(session: AsyncSession, id_: int) -> Question:
    question = await session.scalar(
        select(Question).where(Question.id == id_)
    )
    return question


async def get_questions(session: AsyncSession):
    questions = await session.scalars(
        select(Question)
    )
    return questions


def serialize_question(question: Question) -> dict:
    data = dict(question.__dict__)
    logging.warning(data)
    if code := data.get("code"):
        data["content"] = code
    elif text := data.get("text"):
        data["content"] = text
    return data
