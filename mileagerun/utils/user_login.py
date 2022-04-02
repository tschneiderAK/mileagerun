from passlib.hash import pbkdf2_sha256
from mileagerun.models import User
from mileagerun import db

def verify_password(email: str, password: str):
    if not (email and password):
        return False
    
    password_on_file = User.query.filter_by(email=email).first().password
    if pbkdf2_sha256.verify(password, password_on_file):
        return True
    else:
        return False
