FROM python:3.12-alpine

RUN mkdir /microblog
WORKDIR /microblog

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

LABEL maintainer="squareMic" \
      version="1.0"

CMD flask run --host=0.0.0.0 --port=5000
