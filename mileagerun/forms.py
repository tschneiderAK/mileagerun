from email.charset import Charset
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import *

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email(message='Not a valid email')])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

class Login(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class SampleFlight(FlaskForm):
    origin = StringField('Origin Airport', validators=[DataRequired(), Regexp('^[A-Z]{3}$')])
    destination = StringField('Destination Airport', validators=[DataRequired(), Regexp('[A-Z]{3}')])
    flown_airline = StringField('Airline Flown', validators=[DataRequired(), Regexp("[A-Z]{2}")])
    credit_airline = StringField('Airline Credited', validators=[DataRequired(), Regexp("[A-Z]{2}")])
    fare = StringField('Fare Code', validators=[DataRequired(), Regexp("[A-Z]")])
    submit = SubmitField('Submit')