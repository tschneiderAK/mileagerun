from email.charset import Charset

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField, SelectField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

from mileagerun.utils import get_airlines, get_airports, get_fare_codes, get_flight_type

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[Length(min=1, max=64)])
    last_name = StringField('Last Name', validators=[Length(min=1, max=64)])
    email = EmailField('Email*', validators=[DataRequired(),
                                             Email(message='Not a valid email'),
                                             Length(max=64)])
    password = PasswordField('Password*', validators=[DataRequired(),
                                                     EqualTo('confirm', message='Passwords must match.'),
                                                     Length(min=8, max=20)])
    confirm = PasswordField('Confirm Password*')
    accept_tos = BooleanField('I accept the TOS*', [validators.DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class SampleFlightForm(FlaskForm):
    credit_airline = SelectField(u'Airline Credited', choices=get_airlines())
    origin = SelectField('Origin Airport')
    destination = SelectField('Destination Airport', choices=get_airports())
    flown_airline = SelectField(u'Airline Flown', choices=get_airlines())
    fare = SelectField(u'Fare Code', choices=get_fare_codes(flown_airline))
    type = SelectField(u'Trip Type', choices=get_flight_type(flown_airline, credit_airline))
    submit = SubmitField('Submit')
