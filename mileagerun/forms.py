from email.charset import Charset

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField, SelectField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

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
    origin = StringField('Origin Airport', validators=[DataRequired(), Regexp('^[a-zA-Z]{3}$', message='Input a 3-letter airport code.')], default='LAX')
    destination = StringField('Destination Airport', validators=[DataRequired(), Regexp('^[a-zA-Z]{3}$', message='Input a 3-letter airport code.')], default='JFK')
    flown_airline = SelectField(u'Airline Flown', choices=[('DL', 'Delta'), ('AF', 'Air France'), ('AM', 'Aero Mexico')])
    credit_airline = SelectField(u'Airline Credited', choices=[('DL', 'Delta')])
    fare = StringField('Fare Code', validators=[DataRequired(), Regexp("[a-zA-Z]")], default='Z')
    type = SelectField(u'Trip Type', choices=[('EX-EUROPE', 'Ex-Europe International'), ('INTRA-EUROPE', 'Intra-Europe'), ('STANDARD', 'Standard AM')])
    submit = SubmitField('Submit')
