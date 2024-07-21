#!/bin/sh

# Function to handle starting the application (including DB)
function start_app() {
  # Source the environment variables
  set -o allexport
  source ../../.env.dev.local
  set +o allexport

  # Start the database container in detached mode
  docker-compose -f ../../docker-compose.dev.yml up postgres -d

  # Run the Flask application
  flask run
}

# Function to stop the application and database container
function stop_app() {
  docker-compose -f ../../docker-compose.dev.yml down
}

# # Function to run the application, tests, and then stop it
# function run_test() {
#   set -o allexport
#   # source ../../.env.dev.local
#   source ../../.env.test.local
#   set +o allexport
#   python -m pytest -v
# }

function run_test() {
  set -o allexport
  source ../../.env.test.local
  set +o allexport
  docker-compose -f ../../docker-compose.test.yml up postgres -d

  echo "Waiting for postgres..."
  while ! nc -z "localhost" 54322; do
      echo "sleep 0.1"
      sleep 0.1
  done
  echo "PostgreSQL started"

  flask db upgrade

  python -m pytest -v

  docker-compose -f ../../docker-compose.test.yml down
}

# Check the first argument passed to the script (after the script name)
case "$1" in
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

