from contextlib import asynccontextmanager
from typing import AsyncGenerator

import redis.asyncio as aioredis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import redis
from src.auth.router import router as auth_router
from src.questions.router import router as question_router
from src.grades.router import router as grade_router
from src.answers.router import router as answer_router
from src.grade_requests.router import router as grades_request_router
from src.specializations.router import router as specialization_router
from src.code_execute.router import router as code_execute_router
from src.config import app_configs, settings, STATIC_DIR
from fastapi.staticfiles import StaticFiles


@asynccontextmanager
async def lifespan(_application: FastAPI) -> AsyncGenerator:
    redis_url = str(settings.REDIS_URL)

    pool = aioredis.ConnectionPool.from_url(
        redis_url, max_connections=10, decode_responses=True
    )

    redis.redis_client = aioredis.Redis(connection_pool=pool)
    yield

    if settings.ENVIRONMENT.is_testing:
        return
    # Shutdown
    await pool.disconnect()

app = FastAPI(**app_configs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_origin_regex=settings.CORS_ORIGINS_REGEX,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(question_router, prefix="/questions", tags=["Questions"])
app.include_router(grade_router, prefix="/tests", tags=["Test"])
app.include_router(answer_router, prefix="/answers", tags=["Answers"])
app.include_router(grades_request_router, prefix="/grade-requests", tags=["Grade Requests"])
app.include_router(specialization_router, prefix="/specializations", tags=['Specializations'])
app.include_router(code_execute_router, prefix="/codes", tags=["Codes"])

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
