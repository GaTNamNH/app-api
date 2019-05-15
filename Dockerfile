FROM python:3.7-alpine
MAINTAINER Ngo Hai Nam

ENV PYTHONUNBUFFERED 1

RUN set -e; \
    apk add --no-cache --virtual .build-deps \
    #Linux dependencies
    gcc \
    libc-dev \
    linux-headers \
    # MySQL dependencies 
    mariadb-dev \
    # Python 3 dependencies
    python3-dev \
    # Pillow dependencies
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev \
;

COPY ./requirements.txt /requirements.txt
RUN pip install -r ./requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
