from flask import jsonify
from mileagerun.models import EarningByMiles
from mileagerun.models import EarningByMiles as E
from mileagerun import db

def get_partners():
    partners = {}
    for airline in db.session.query(E.flown_airline).distinct().all():
        partners[airline[0]] = [r[0] for r in db.session.query(E.credit_airline).distinct().all()]

    partners = jsonify(partners)
    return partners