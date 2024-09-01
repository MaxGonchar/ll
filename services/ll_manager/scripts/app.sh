#!/bin/sh

validate_env() {
  env=$1

  if [ "$env" != "dev" ] && [ "$env" != "test" ] && [ "$env" != "test_integ" ]; then
    echo "Invalid environment argument. Choose 'dev', 'test', or 'test_integ'."
    exit 1
  fi
}

load_env_vars() {
  env=$1
  validate_env "$env"
  env_vars_file="../../envs/.env.${env}"

  echo "Loading environment variables from $env_vars_file"
  set -o allexport
  . "$env_vars_file"
  set +o allexport
}

wait_for_postgres() {
  docker_compose_file=$1
  max_attempts=60
  attempt=1

  echo "Waiting for postgres..."

  until docker-compose -f "$docker_compose_file" exec -T postgres pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB" || [ $attempt -eq $max_attempts ]; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
    attempt=$((attempt+1))
  done

  if [ $attempt -eq $max_attempts ]; then
    >&2 echo "Max connection attempts reached. Exiting..."
    exit 1
  fi

  echo "Postgres started"
}

app_run() {
  env=$1
  load_env_vars "$env"
  docker_compose_file="../../docker-compose.${env}.yml"

  docker-compose -f "$docker_compose_file" up postgres -d

  wait_for_postgres "$docker_compose_file"

  echo "Set up LL db"
  flask db upgrade

  flask run

  if [ "$env" = "test" ]; then
    docker-compose -f "$docker_compose_file" down -v
  else
    docker-compose -f "$docker_compose_file" down
  fi
}

app_run_dev() {
  app_run dev
}

app_run_test() {
  app_run test
}

# TODO: move tests running to a separate script
setup_unit_test_env() {
  #TODO: move to constants
  docker_compose_file="../../docker-compose.test.yml"
  load_env_vars test

  docker-compose -f "$docker_compose_file" up -d postgres

  wait_for_postgres "$docker_compose_file"

  echo "Set up LL db"
  flask db upgrade

  echo "$docker_compose_file"
}

tear_down_test_env() {
  load_env_vars test
  docker_compose_file="../../docker-compose.test.yml"
  echo "Tearing test env down"
  docker-compose -f "$docker_compose_file" down -v
}

run_unit_test() {
  setup_unit_test_env

  echo "Running tests"
  pytest tests/unit -v
  coverage report

  echo "Tearing down LL db"
  tear_down_test_env
}

upgrade_db() {
  env=$1
  load_env_vars "$env"
  docker_compose_file="../../docker-compose.${env}.yml"

  wait_for_postgres "$docker_compose_file"

  echo "Upgrading LL db"
  flask db upgrade
  echo "LL db upgraded"
}

setup_integ_test_env() {
  load_env_vars test_integ
  docker_compose_file="../../docker-compose.test.yml"

  echo "Building docker images"
  docker-compose -f "$docker_compose_file" up -d --build

  echo "Waiting for ll_manager..."
  until curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/health | grep -q 200; do
      >&2 echo "ll_manager is unavailable - sleeping"
      sleep 1
  done
}

run_integ_test() {
  setup_integ_test_env

  echo "Running tests"
  pytest tests/integration -v

  tear_down_test_env
}

case "$1" in
  dev)
    app_run_dev
    ;;
  test)
    app_run_test
    ;;
  setup_unit_test_env)
    setup_unit_test_env
    ;;
  setup_integ_test_env)
    setup_integ_test_env
    ;;
  unit_test)
    run_unit_test
    ;;
  teardown_test_env)
    tear_down_test_env
    ;;
  integ_test)
    run_integ_test
    ;;
  upgrade)
    upgrade_db
    ;;
  *)
    echo "Invalid argument: '$1'"
    echo "Usage: ./app.sh {dev|test|unit_test|upgrade}"
    ;;
esac
