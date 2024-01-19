FROM python:3.11-slim

RUN mkdir -p /usr/src/app

COPY requirements.txt /usr/src/marski-group-solver/
RUN pip install -U pip
RUN pip install -r /usr/src//marski-group-solver/requirements.txt
COPY . /usr/src//marski-group-solver
WORKDIR /usr/src//marski-group-solver
RUN pip install -e .
CMD ["make"]