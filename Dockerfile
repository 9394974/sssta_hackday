FROM daocloud.io/python:3-onbuild

MAINTAINER sssta_hackday "crazy_leaves@outlook.com"

RUN mkdir -p /sssta_hackday

WORKDIR /sssta_hackday

COPY . /sssta_hackday

RUN apt-get update && apt-get install sqlite3

RUN pip3 install -r requirements.txt

EXPOSE 15000

CMD python3 manage.py
