#!/bin/sh

set -o allexport
source ../../.env.test.local
set +o allexport
docker-compose -f ../../docker-compose.test.yml up postgres -d

POSTGRES_CONTAINER=$(docker-compose -f ../../docker-compose.test.yml ps -q postgres)

echo "Waiting for postgres to be ready..."
while ! docker exec "$POSTGRES_CONTAINER" psql -h localhost -p 5432 -U ll_test_user -d ll_test -c "SELECT 1;" > /dev/null 2>&1; do
echo "  Postgres not ready yet..."
sleep 5
done
echo "Postgres is ready!"

echo "Upgrade DB..."
flask db upgrade
echo "Done"

echo "Start tests..."
python -m pytest -v

docker-compose -f ../../docker-compose.test.yml down -v
