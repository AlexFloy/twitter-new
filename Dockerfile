FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /twitter/

COPY requirements.txt . /twitter/

RUN pip install --no-cache-dir --verbose -r requirements.txt

COPY . /twitter/