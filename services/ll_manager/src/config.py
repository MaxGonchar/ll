import os

basedir = os.path.abspath(os.path.dirname(__file__))


def _get_db_uri() -> str:
    return (
        "postgresql+psycopg2://"
        f"{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}"
        f"@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}"
        f"/{os.environ['POSTGRES_DB']}"
    )


class Config:
    SQLALCHEMY_DATABASE_URI = _get_db_uri()
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

