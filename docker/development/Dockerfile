FROM python:3.9.4-alpine

RUN apk add --update --no-cache --virtual .build-deps \
  build-base \
  linux-headers \
  libffi-dev \
  python3-dev \
  openssl-dev \
  cargo \
  git

RUN python -m pip install --upgrade pip && \
    pip install poetry

RUN mkdir /src
WORKDIR /src
