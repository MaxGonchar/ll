from datetime import datetime

from src.extensions import db
from src.models.user import User


def add_user(user) -> None:
    db.session.add(
        User(
            first=user.first,
            last=user.last,
            email=user.email,
            role="default_role",
            password_hash="qweqweqwe",
            last_login=datetime.now()
        ),
    )
    db.session.commit()
