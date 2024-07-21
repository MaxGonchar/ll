import os

from flask import Response, jsonify
from flask_migrate import Migrate
from flask_openapi3 import OpenAPI  # type: ignore [import-untyped]
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text

from src.api.auth import auth_api
from src.extensions import db
# for alembic
from src.models import User

app = OpenAPI(__name__)
app.config.from_object("src.config.Config")

db.init_app(app)
Migrate(app, db, directory=os.path.join("src", "migrations"))

app.register_api(auth_api)

@app.get("/")
def hello_world() -> Response:
    return jsonify(hello="world!!!")
