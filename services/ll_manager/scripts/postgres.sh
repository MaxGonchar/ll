set -o allexport
source ../../envs/.env.dev
set +o allexport
docker-compose -f ../../docker-compose.dev.yml exec postgres psql --username=${POSTGRES_USER} --dbname=${POSTGRES_DB}