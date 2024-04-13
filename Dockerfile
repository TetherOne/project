FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt

COPY menu /menu

WORKDIR /menu

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN adduser --disabled-password menu-user

USER menu-user