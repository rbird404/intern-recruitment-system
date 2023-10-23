from pydantic import Field, ConfigDict
from pydantic import BaseModel

from src.auth.utils import UserRoleType


class AuthUser(BaseModel):
    username: str
    password: str = Field(min_length=6, max_length=128)


class UserCreate(AuthUser):
    first_name: str | None
    last_name: str | None
    email: str
    role: UserRoleType | None = None
    model_config = ConfigDict(from_attributes=True)


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: str | None
    last_name: str | None
    role: str | None



class TokenPair(BaseModel):
    access_token: str
    refresh_token: str


class RefreshToken(BaseModel):
    refresh_token: str
