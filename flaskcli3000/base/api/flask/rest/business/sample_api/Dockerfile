 
FROM python:3.7-alpine

RUN apk add --no-cache --update python3-dev gcc build-base

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

RUN pytest

EXPOSE 5000

ENTRYPOINT ["sh", "entrypoint.sh"]