from src.extensions import db
from src.models.user import User


# TODO: handle user already exists
def add_user(user: User) -> None:
    db.session.add(user)
    db.session.commit()
