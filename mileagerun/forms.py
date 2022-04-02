from email.charset import Charset
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import *

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email(message='Not a valid email')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match.')])
    confirm = PasswordField('Confirm Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Submit')

class Login(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class SampleFlight(FlaskForm):
    origin = StringField('Origin Airport', validators=[DataRequired(), Regexp('^[a-zA-Z]{3}$', message='Input a 3-letter airport code.')], default='LAX')
    destination = StringField('Destination Airport', validators=[DataRequired(), Regexp('^[a-zA-Z]{3}$', message='Input a 3-letter airport code.')], default='JFK')
    flown_airline = StringField('Airline Flown', validators=[DataRequired(), Regexp("[a-zA-Z]{2}")], default='AF')
    credit_airline = StringField('Airline Credited', validators=[DataRequired(), Regexp("a-z[A-Z]{2}")], default='AF')
    fare = StringField('Fare Code', validators=[DataRequired(), Regexp("[A-Z]")], default='Z')
    submit = SubmitField('Submit')
