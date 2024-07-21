from datetime import datetime
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, TIMESTAMP

from src.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)
    last: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)
    email: Mapped[str] = mapped_column(VARCHAR(50), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(VARCHAR(15), nullable=False)
    password_hash: Mapped[str] = mapped_column(db.String(70), nullable=False)
    properties: Mapped[dict] = mapped_column(JSON, nullable=False, default={})
    added: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=func.now())
    updated: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())
    last_login: Mapped[datetime] = db.Column(TIMESTAMP, nullable=False)
