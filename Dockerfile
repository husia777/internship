FROM python:3.9

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN sudo apk update \
    && sudo apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .