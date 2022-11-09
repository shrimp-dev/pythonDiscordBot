FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN apk add --no-cache ffmpeg
WORKDIR /app
COPY requirements.txt requirements.txt
COPY . /app
RUN pip3 install -r requirements.txt
