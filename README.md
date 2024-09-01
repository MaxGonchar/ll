[![ll_manager_tests](https://github.com/MaxGonchar/ll/actions/workflows/ll_manager_tests.yaml/badge.svg)](https://github.com/MaxGonchar/ll/actions/workflows/ll_manager_tests.yaml)

## Knowledge base
python:
- [flask](https://flask.palletsprojects.com/en/3.0.x/)
- [flask-openapi3](https://luolingchun.github.io/flask-openapi3/v3.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/#why-use-flask-migrate-vs-alembic-directly)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/index.html)

db:
- [postgres](https://www.postgresql.org/)

## Development

### Set up
required:
- python 3.11
- docker

#### set up an environment:
- `cd services/ll_manager`
- `python3.11 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `pip install -r dev_requirements.txt`

provide execute permission to `app.sh`, `postgres.sh`
`chmod +x app.sh`
`chmod +x postgres.sh`

#### run app in dev mode
`./scripts/app.sh dev`
- up postgres docker container with volume
- apply migrations
- run app
- when app stop, down the db container

#### run app in test mode
`./scripts/app.sh test`
- up postgres docker container with volume
- apply migrations
- run app
- when app stop, down the db container, remove volume
in test mode you can tun integration tests\
`pytest tests/integration`

#### run unit tests
`./scripts/app.sh unit_test`
- up postgres docker container with volume
- apply migrations
- run unit tests
- down the db container
- remove volume

#### run integration tests
`./scripts/app.sh integ_test`
- up postgres docker container with volume
- build and up app container (tag: "test")
- run integration tests
- down all containers
- remove volume

#### access postgres
`./scripts/postgres.sh`\
to exit\
`Ctrl + P` followed by `Ctrl + Q`

#### type checking
`mypy src`

#### linter
`ruff format`
`ruff check --fix`
`ruff check`

---------------------------------------------------------------------------------------------------

### Tests
`python -m pytest -v`

### Formatter / Linter / Typing
- `black .`
- `ruff check --fix`
- `mypy .`

### Development in Docker

#### Run App
- `docker-compose build`
- `docker-compose up -d`
- `docker-compose up -d --build`

#### See Docker Logs
Check for errors in the logs - `docker-compose logs -f`.

#### Run Tests
`docker-compose exec web python -m pytest -v`

#### Stop App
`docker-compose down`