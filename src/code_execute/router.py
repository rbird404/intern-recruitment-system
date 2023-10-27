from typing import List
from fastapi import APIRouter

from src.auth import service
from src.code_execute.schemas import UserCode, CodeUserResult
from src.database import AsyncDbSession
from src.grade_requests import service
from src.code_execute import service


router = APIRouter()


@router.post("/{code_id}", status_code=200, response_model=List[CodeUserResult])
async def code_execute(session: AsyncDbSession, code_id: int, user_code: UserCode):
    test_cases = await service.get_test_cases(session, code_id)
    results = []
    for test_case in test_cases:
        results.append(
            await service.run_test_case(
                test_case,
                user_code.language,
                user_code.code
            )
        )
    return results
