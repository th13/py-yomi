FROM ubuntu:17.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3.6 python3-pip

WORKDIR /code
ADD ./requirements.txt /code
RUN python3.6 -m pip install -r requirements.txt
ADD . /code

EXPOSE 8080