FROM python:3.12-slim

RUN apt-get update
RUN apt-get install -y build-essential

COPY requirements.txt /opt/app/
RUN pip install -r /opt/app/requirements.txt
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -e .
RUN make all