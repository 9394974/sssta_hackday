FROM python:3

MAINTAINER Qinka <qinka@live.com>

RUN mkdir -p /app

COPY  /app/requestments

RUN pip3 install -r /app/requestments
RUN apt