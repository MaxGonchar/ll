#!/bin/sh

echo "Waiting for postgres..."
while ! nc -z postgres 5432; do
    echo "sleep 0.1"
    sleep 0.1
done
echo "PostgreSQL started"

echo "Upgrading LL db"
flask db upgrade

echo "Start app"
flask run  -h 0.0.0.0
