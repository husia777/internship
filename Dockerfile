FROM python:3.9

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN  apt update \
     &&  apt add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --upgrade pip
COPY . .