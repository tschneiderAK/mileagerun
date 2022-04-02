from sre_constants import SUCCESS
from passlib.hash import pbkdf2_sha256
from mileagerun import db
from mileagerun.models import User
from flask import flash

def new_user_registration(form):
    email = form.email.data
    if User.query.filter_by(email=email).first():
        return flash(f"Email {email} is already in use. Please login.")
    registration = User(first_name = form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            password=pbkdf2_sha256.hash(form.password.data))
    db.session.add(registration)
    db.session.commit()
    return flash('User registration successful!', category=SUCCESS)