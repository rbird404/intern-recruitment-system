import logging

import httpx
from sqlalchemy import select

from src.code_execute.schemas import CodeExecutorResult, CodeUserResult
from src.config import CODE_EXECUTOR_URL
from src.database import AsyncDbSession
from src.questions.models import TestCase


async def get_test_cases(session: AsyncDbSession, code_id: int):
    test_cases = await session.scalars(
        select(TestCase).where(TestCase.code_id == code_id)
    )
    return test_cases


async def run_test_case(test_case: TestCase, language: str, code: str):
    async with httpx.AsyncClient(base_url=CODE_EXECUTOR_URL) as client:
        response = await client.post(
            '/code_executor/execute',
            json={
                "language": language,
                "code": code,
                "input": test_case.input
            },
            timeout=100
        )
        if response.status_code == 200:
            result = CodeExecutorResult(**response.json())
            if test_case.output == result.output:
                result = CodeUserResult(**result.model_dump(), status=1)
            else:
                result = CodeUserResult(**result.model_dump(), status=0)
            return result

        return CodeUserResult(status=2, time=1.0)
