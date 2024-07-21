## Knowledge base
python:
- [flask](https://flask.palletsprojects.com/en/3.0.x/)
- [flask-openapi3](https://luolingchun.github.io/flask-openapi3/v3.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/#why-use-flask-migrate-vs-alembic-directly)

db:
- [postgres](https://www.postgresql.org/)

## Development

### Set up
required:
- python 3.11
- docker

Create `.env.dev` and `.env.dev.local` file with env vars you need (look at `.env.dev.sample`)

For developing from local station:
#### set up an environment:
- `cd services/ll_manager`
- `python3.11 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `pip install -r dev_requirements.txt`

#### set up env vars:
In `.env.dev.local`
replace POSTGRES_HOST with "localhost"
replace POSTGRES_PORT with port you want

provide execute permission to `app.sh`, `postgres.sh`
`chmod +x app.sh`
`chmod +x postgres.sh`

**./app.sh run** - up db in container and start app
**./app.sh stop** - down db container
**./app.sh test** - run tests


#### apply db migrations
`flask db upgrade`

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