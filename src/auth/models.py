from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import (
    Boolean,
    String,
    LargeBinary,
    UUID,
    DateTime,
    ForeignKey,
    Integer
)

from src.database import Base


class UserRole(Base):
    __tablename__ = "user_roles"
    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    name = mapped_column(String, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    # TODO добавить фото
    first_name = mapped_column(String)
    last_name = mapped_column(String)
    email = mapped_column(String, unique=True, nullable=False)
    username = mapped_column(String, unique=True, nullable=False)
    password = mapped_column(LargeBinary, nullable=False)
    is_admin = mapped_column(Boolean, default=False, server_default="false", nullable=False)
    telegram_id = mapped_column(String, nullable=True)
    chat_id = mapped_column(String, nullable=True)

    # relationships
    role_id = mapped_column(ForeignKey("user_roles.id", ondelete="SET NULL"), nullable=True)
    role = relationship(UserRole)


class WhitelistedToken(Base):
    __tablename__ = 'whitelisted_tokens'

    jti = mapped_column(UUID, primary_key=True)
    expires_at = mapped_column(DateTime, nullable=False)

    # relationships
    user_id = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
