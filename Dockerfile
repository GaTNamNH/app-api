FROM python:3.7-alpine
MAINTAINER Ngo Hai Nam

ENV PYTHONUNBUFFERED 1

RUN set -e; \
    apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    linux-headers \
    mariadb-dev \
    python3-dev \
    postgresql-dev \
;

COPY ./requirements.txt /requirements.txt
RUN pip install -r ./requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
