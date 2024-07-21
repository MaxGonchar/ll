from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os

import src.repos.auth_repo as subj
from src import app


class User:
    def __init__(self, first, last, email) -> None:
        self.first = first
        self.last = last
        self.email = email


def _get_user(email):
    print(os.environ["POSTGRES_USER"])
    print(os.environ["POSTGRES_PASSWORD"])
    print(os.environ["POSTGRES_HOST"])
    print(os.environ["POSTGRES_DB"])
    print(os.environ["POSTGRES_PORT"])
    engine = create_engine(f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_HOST"]}:{os.environ["POSTGRES_PORT"]}/{os.environ["POSTGRES_DB"]}')

    with engine.connect() as con:
        users = con.execute(text("SELECT * FROM users WHERE email=:email"), {"email": email}).all()
    
    return users
        


def test_add():
    email = "email-1"
    with app.app_context():
        subj.add_user(User("firs", "last", email))
    users = _get_user(email)
    print(users[0])

    assert 1 == 2
