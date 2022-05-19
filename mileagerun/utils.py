from json import dumps

from flask import flash, jsonify, redirect, url_for
from haversine import haversine, Unit
from passlib.hash import pbkdf2_sha256

from mileagerun import db
from mileagerun.models import EarningByMiles as E, Airlines
from mileagerun.models import User, Airports


def get_partners():
    """
    Gets airline partner mappings.

    :return: JSON object of partners, with each airline having a list of other airlines to which they can credit miles earned.
    :rtype: JSON

    """
    partners = []
    for airline in db.session.query(E.flown_airline).distinct().all():
        partnerObj = {}
        partnerObj['flown'] = airline[0]
        partnerObj['credited'] = [r[0] for r in db.session.query(E.credit_airline).distinct().all()]
        partners.append(partnerObj)

    print(partners)
    return jsonify({'partnerships' : partners})


def miles_earned(distance_flown: float, credit_airline: str, flown_airline: str,flight_type: str, fare_code: str):
    """
    Calculates redeemable miles, elite qualifying miles, and elite qualifying dollars earned for a flight.
    
    :param float distance_flown: Distance flown in miles.
    :param str credit_airline:   2-letter IATA code for airline credited to. Case insensitive.
    :param str flown_airline:    2-letter IATA code for airline flown. Case insensitive.
    :param str fare_code:        Single-letter fare code (A-Z). Case insensitive.
    :param str flight_type:      Type of flight, will vary by airline flown.
    :return: Earned mqm, eqm, eqd.
    :rtype: :type mapping: dict(str, int)

    """
    # Query multiplier values mapper to the 'Earning' model.
    multipliers = db.session.query(E).filter(E.credit_airline==credit_airline.upper()).\
                                                filter(E.flown_airline==flown_airline.upper()).\
                                                filter(E.flight_type==flight_type).\
                                                filter(E.fare_code==fare_code.upper()).first()

    rdm = round(distance_flown * multipliers.total_rdm_mult) # Redeemable miles (rdm) earned in the credit airline's frequent flyer currency
    eqm = round(distance_flown * multipliers.eqm_mult)       # Elite qualifying miles as defined by the credit airline
    eqd = round(distance_flown * multipliers.eqd_mult)       # Elite qualifying dollars, if applicable, for credit airline.
    earnings = {'rdm': rdm,
                'eqm': eqm,
                'eqd': eqd}
    return earnings

def calc_distance(origin, destination):
    """
    Calculate distance in miles between two airports.
    
    :param str origin:      3-letter IATA code for an airport. Case insensitive.
    :param str destination: 3-letter IATA code for an airport. Case insensitive.
    :return: Distance between airports in miles.
    :rtype: float

    """
    origin_model = db.session.query(Airports).filter_by(iata_code=origin.upper()).first()
    dest_model = db.session.query(Airports).filter_by(iata_code=destination.upper()).first()

    if not (origin_model and dest_model):
        return 'Origin or destination not found.'

    origin_coords = (origin_model.lat_decimal, origin_model.lon_decimal)
    dest_coords = (dest_model.lat_decimal, dest_model.lon_decimal)

    if not (origin_coords and dest_coords):
        return 'Coordinates not found'

    # Use haversine formula to get distance between coords.
    distance = round(haversine(origin_coords, dest_coords, unit=Unit.MILES))
    return distance


def new_user_registration(form):
    """
    Registers a new user to the database.

    :param form form: Form data from RegistrationForm.

    """

    email = form.email.data
    if User.query.filter_by(email=email).first():
        flash(f"Email {email} is already in use. Please login.")
        return redirect(url_for('login'))
    registration = User(first_name = form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            password=pbkdf2_sha256.hash(form.password.data))
    db.session.add(registration)
    db.session.commit()
    return flash('User registration successful!')

def authenticate_password(email: str, password: str):
    """
    Athenticates the input password matches the password on file for the email provided.
    
    :param str email: Email address for the account being logged in to.
    :param str password: Password to be authenticated.
    :return: Authentication status.
    :rtype: bool

    """

    if not (email and password):
        return False
    
    password_on_file = User.query.filter_by(email=email).first().password
    if pbkdf2_sha256.verify(password, password_on_file):
        return True
    else:
        return False

def get_airlines():
    airlines = []
    for iata_code, full_name in db.session.query(Airlines.iata_code, Airlines.full_name):
        airlines.append((iata_code, full_name))
    return airlines