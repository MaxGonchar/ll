set -o allexport
source ../../.env.dev
set +o allexport
docker-compose -f ../../docker-compose.dev.yml exec postgres psql --username=${POSTGRES_USER} --dbname=${POSTGRES_DB}