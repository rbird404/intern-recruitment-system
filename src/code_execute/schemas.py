from pydantic import BaseModel


class UserCode(BaseModel):
    language: str
    code: str


class CodeExecutorResult(BaseModel):
    output: str | None = None
    errors: str | None = None
    time: float


class CodeUserResult(CodeExecutorResult):
    status: int

