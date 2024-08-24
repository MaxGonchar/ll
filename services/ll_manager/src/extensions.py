import json
from functools import partial

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(
    engine_options={
        "json_serializer": partial(json.dumps, ensure_ascii=False),
    },
)
