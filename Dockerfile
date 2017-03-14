FROM python:3

MAINTAINER Qinka <qinka@live.com>

RUN mkdir -p /app

COPY requestments.txt /app/requestments

RUN pip3 install -r /app/requestments
RUN apt install libsqlite3-0

COPY . /app/

EXPOSE 15000
CMD python3 /app/manage.py
