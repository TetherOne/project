FROM python:3.11.4-slim

COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt

COPY menu /menu

WORKDIR /menu

EXPOSE 8000
