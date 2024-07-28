#!/bin/sh

function wait_for_postgres() {
  echo "Waiting for postgres..."
  until docker-compose -f ../../docker-compose.dev.yml exec postgres pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB"; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
  done
  echo "Postgres started"
}

function upgrade_db() {
  set -o allexport
  source ../../envs/.env.dev.local
  set +o allexport

  wait_for_postgres

  echo "Upgrading LL db"
  flask db upgrade
  echo "LL db upgraded"
}

function start_app() {
  set -o allexport
  source ../../envs/.env.dev.local
  set +o allexport

  docker-compose -f ../../docker-compose.dev.yml up postgres -d

  flask run
}

function stop_app() {
  docker-compose -f ../../docker-compose.dev.yml down
}


function run_test() {
  set -o allexport
  source ../../envs/.env.test.local
  set +o allexport
  docker-compose -f ../../docker-compose.test.yml up postgres -d

  wait_for_postgres

  echo "Set up LL db"
  flask db upgrade
  echo "LL db set up"

  echo "Running tests"
  python -m pytest -v

  echo "Tearing down LL db"
  docker-compose -f ../../docker-compose.test.yml down
}

# Check the first argument passed to the script (after the script name)
case "$1" in
  upgrade)
    upgrade_db
    ;;
  run)
    start_app
    ;;
  stop)
    stop_app
    ;;
  test)
    run_test
    ;;
  *)
    echo "Invalid argument: '$1'"
    echo "Usage: ./app.sh {run|stop|test}"
    ;;
esac
