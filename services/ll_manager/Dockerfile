# pull official base image
FROM python:3.11.3-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./dev_requirements.txt /usr/src/app/dev_requirements.txt
RUN pip install -r requirements.txt
# TODO(MaxGonchar): remove dev_requirements.txt
RUN pip install -r dev_requirements.txt

# copy project
COPY ./src /usr/src/app/src
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# # run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
