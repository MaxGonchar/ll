import os
from datetime import timedelta
from pathlib import Path

basedir = Path(__file__).resolve().parent


def _get_db_uri() -> str:
    return (
        "postgresql+psycopg2://"
        f"{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}"
        f"@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}"
        f"/{os.environ['POSTGRES_DB']}"
    )


class Config:
    SQLALCHEMY_DATABASE_URI = _get_db_uri()
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
    # TODO(MaxGonchar): move to env vars
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
