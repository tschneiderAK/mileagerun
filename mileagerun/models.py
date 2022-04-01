from mileagerun import db
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    __tablename__ = "users"
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email


class Flight(db.Model):
    __table__ = db.Table('flights', db.metadata, autoload=True, autoload_with=db.engine)

earnings = db.Table('earning_by_miles', db.metadata, autoload=True, autoload_with=db.engine)

airlines = db.Table('airlines', db.metadata, autoload=True, autoload_with=db.engine)

airports = db.Table('airports', db.metadata, autoload=True, autoload_with=db.engine)
