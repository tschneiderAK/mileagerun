FROM python:3.10.4

WORKDIR /app

ADD . /app/

RUN pip install -r requirements.txt

RUN mkdir /var/log/uwsgi

CMD ["uwsgi", "app.ini"]
