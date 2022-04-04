from flask import redirect, render_template, request, url_for, session, flash

from mileagerun import app, db
from mileagerun.forms import LoginForm, RegistrationForm, SampleFlightForm
from mileagerun.models import EarningByMiles, User
from mileagerun.utils import authenticate_password, calc_distance, get_partners, miles_earned, new_user_registration 



@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def home():
    form = SampleFlightForm()    
    form.validate_on_submit()
    if request.method == 'POST':
        distance = calc_distance(origin=form.origin.data, destination=form.destination.data)
        earnings = miles_earned(distance_flown=distance,
                                credit_airline=form.credit_airline.data,
                                flown_airline=form.flown_airline.data,
                                flight_type=form.type.data,
                                fare_code=form.fare.data)
        return render_template('index.html', distance=distance, earnings=earnings, form=form, partners=get_partners())
    return render_template('index.html', distance=0, earnings=None, form=form, partners=get_partners())


@app.route('/view')
def view():
    return render_template('view.html', values=EarningByMiles.query.all())


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user_registration(form)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        if authenticate_password(email=email, password=password):
            session.permanent = True
            session['email'] = email
            flash(f"Successfully logged in.")
            return redirect(url_for('userhome'))
        else:
            flash(f"Incorrect username or password.")
            return redirect(url_for('login')) 

    else:
        if 'user' in session:
            user = session['user']
            flash(f"Logged in as {user}.")
            return redirect(url_for('userhome'))
        return render_template('login.html', form=form)

@app.route('/userhome', methods=['POST', 'GET']) 
def userhome():
    if 'email' in session:
        email = session['email']
        return render_template('userhome.html', email=email)
    else:
        return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f"You have been logged out, {user}.", "info")
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/earnings')
def earnings():
    values = db.session.query(EarningByMiles).all()
    return render_template('earnings.html', values=values)