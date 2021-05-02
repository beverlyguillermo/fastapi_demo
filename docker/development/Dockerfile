FROM python:3.9.4-alpine

EXPOSE 8000

RUN apk add --update --no-cache --virtual .build-deps \
  build-base \
  linux-headers \
  libffi-dev \
  python3-dev \
  git

RUN mkdir /src
WORKDIR /src

COPY requirements.txt .
RUN  python3 -m venv /venv \
     && . /venv/bin/activate \
     && python3 -m pip install --upgrade pip \
     && pip install -r requirements.txt

COPY docker/development/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 755 /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]


