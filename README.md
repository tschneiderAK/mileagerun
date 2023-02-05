# Mileagerun
Calculates frequent flyer miles earned based on the earning airline and the marketing/operating airline.

## Installation and Configuration
### Extensions

- SQL ORM:  [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.5/)

- Forms:    Flask-WTForms

### Installation

#### Install with pip:

```
pip install -r requirements.txt
```

### Environment Configuration

Mileagerun requires the following environment variables to be configured prior to deployment:

| Variable name   | Description                         |
|-----------------|-------------------------------------|
|DATABASE_HOST    | Host location for your database.    |
|DATABASE_USER    | Username for databse.               |
|DATABASE_PASSWORD| Password for database.              |  
|DATABASE_NAME    | Database name.                      |
|DATABASE_URI     | URI for database at host location.  |
|FLASK_SECRET_KEY | Flask secret key, can be any key.   |


### Local Deployment

The flask application can be deployed locally by calling run.py within the Flask directory:

```
$ python3 run.py
```

To run in debug mode, use the 'True' flag as a CLA:

```
$ python3 run.py True
```

### UWSGI Deployment

Uses app.ini for deployment options.
```
uwsgi run.py app.ini
```

### Docker Deployment

#### Docker Images Required:

tschneiderak/mileagerun:flask
tschneiderak/mileagerun:nginx

#### Using docker compose

```
$ docker compose pull up
```

### Cloud Hosted Usage:

Public cloud host not currently available.
