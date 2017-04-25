FROM ubuntu:17.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3.6 python3-pip

RUN python3.6 -m pip install pika
ADD ./lib /code/lib
