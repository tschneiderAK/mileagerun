from sqlalchemy import ForeignKey
from app import db
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    __tablename__ = 'users'
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

class FlightType(db.Model):
    __tablename__ = 'flight_types'
    _id = db.Column('id', db.Integer, primary_key=True)
    airline = db.Column(db.String(64), ForeignKey('airlines.iata_code'), nullable=False)
    description = db.Column(db.String(64), nullable=False)


class Flight(db.Model):
    __table__ = db.Table('flights', db.metadata, autoload=True, autoload_with=db.engine)


class EarningByMiles(db.Model):
    __table__ = db.Table('earning_by_miles', db.metadata, autoload=True, autoload_with=db.engine)


class Airlines(db.Model):
    __table__ = db.Table('airlines', db.metadata, autoload=True, autoload_with=db.engine)


class Airports(db.Model):
    __table__ = db.Table('airports', db.metadata, autoload=True, autoload_with=db.engine)

class FareCodes(db.Model):
    __tablename__ = 'fare_codes'
    _id = db.Column('id', db.Integer, primary_key=True)
    airline = db.Column(db.String(2), ForeignKey('airlines.iata_code'), nullable=False)
    code = db.Column(db.String(2), nullable=False)


