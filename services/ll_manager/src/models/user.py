from datetime import datetime
from uuid import uuid4

from sqlalchemy import TIMESTAMP, VARCHAR
from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash

from src.extensions import db


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)
    last: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)
    email: Mapped[str] = mapped_column(VARCHAR(50), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(VARCHAR(15), nullable=False)
    password_hash: Mapped[str] = mapped_column(db.String(200), nullable=False)
    properties: Mapped[dict] = mapped_column(JSON, nullable=False, default={})
    added: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=func.now())
    updated: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())
    last_login: Mapped[datetime] = db.Column(TIMESTAMP, nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def hash_psw(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_psw(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
