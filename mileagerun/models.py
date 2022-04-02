from mileagerun import db
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    __tablename__ = "users"
    _id = db.Column('id', db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    password = db.Column(db.String(256))
    email = db.Column(db.String(64))

    def __init__(self, first_name, last_name, email, password) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Flight(db.Model):
    __table__ = db.Table('flights', db.metadata, autoload=True, autoload_with=db.engine)

earnings = db.Table('earning_by_miles', db.metadata, autoload=True, autoload_with=db.engine)

airlines = db.Table('airlines', db.metadata, autoload=True, autoload_with=db.engine)

airports = db.Table('airports', db.metadata, autoload=True, autoload_with=db.engine)
