FROM python:3.10.1-bullseye
LABEL Thiago Teixeira Magalhães <thiago.magalhaes@gmail.com>

ADD requirements.txt .
ADD api.py .

RUN apt-get update && apt-get install -y unixodbc-dev

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt 

CMD ["gunicorn", "--log-level", "debug", "--bind", "0.0.0.0:8000", "api:app"]

EXPOSE 8000
