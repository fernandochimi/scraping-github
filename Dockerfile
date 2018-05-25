FROM python:3.6.4-alpine

RUN echo http://mirror.yandex.ru/mirrors/alpine/v3.4/main > /etc/apk/repositories; \
    echo http://mirror.yandex.ru/mirrors/alpine/v3.4/community >> /etc/apk/repositories

RUN apk update && \
	apk add git \
	build-base \
	libffi-dev \
	libxslt-dev \
	openssl-dev \
	tzdata

RUN echo "America/Sao_Paulo" > /etc/timezone

RUN mkdir -p /scraping-github

WORKDIR /scraping-github

COPY ./requirements.txt /scraping-github/

RUN pip install -r requirements.txt

ADD . /scraping-github/