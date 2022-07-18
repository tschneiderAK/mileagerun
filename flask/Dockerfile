FROM python:3.10.4

WORKDIR /app

ADD . /app/

RUN pip install -r requirements.txt

RUN mkdir /var/log/uwsgi
RUN touch /var/log/uwsgi/uwsgi_access.log
RUN touch /var/log/uwsgi/uwsgi_error.log

CMD ["uwsgi", "app.ini"]