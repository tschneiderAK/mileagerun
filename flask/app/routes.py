import json

from flask import redirect, render_template, request, url_for, session, flash, jsonify

from app import app, db, utils
from app.forms import LoginForm, RegistrationForm, SampleFlightForm
from app.models import EarningByMiles as E, User, Airlines
from app.utils import authenticate_password, calc_distance, get_partners, miles_earned, new_user_registration 



@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def home():
    form = SampleFlightForm()    
    
    if request.method == 'POST' and form.submit(): 
        print('form submit')
        distance = calc_distance(origin=form.origin.data, destination=form.destination.data)
        earnings = miles_earned(distance_flown=distance,
                                credit_airline=form.credit_airline.data,
                                flown_airline=form.flown_airline.data,
                                flight_type=form.type.data,
                                fare_code=form.fare.data)
        return render_template('index.html', distance=distance, earnings=earnings, form=form, partners='Partners')
    return render_template('index.html', distance=0, earnings=None, form=form, partners='Partners')


@app.route('/view')
def view():
    return render_template('view.html', values=E.query.all())


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
    values = db.session.query(E).all()
    return render_template('earnings.html', values=values)

@app.route('/data/flown-to-credited/<flown>')
def flown_to_credit(flown):
    credit_airlines = [('None', 'Select a credit airline')]
    for iata_code, full_name in  db.session.query(E.credit_airline, Airlines.full_name).\
            filter_by(flown_airline=flown).\
            join(Airlines, E.credit_airline==Airlines.iata_code).\
            distinct().all():
        credit_airlines.append((iata_code, full_name))
    print(credit_airlines)
    return jsonify({'credit airlines' : credit_airlines})

@app.route('/data/credited-to-flown/<credited>')
def credit_to_flown(credited):
    partner_airlines = []
    other_airlines =[]
    for iata_code, full_name in  db.session.query(E.flown_airline, Airlines.full_name).\
            filter_by(credit_airline=credited).\
            join(Airlines, E.flown_airline==Airlines.iata_code).\
            distinct().all():
        partner_airlines.append((iata_code, full_name))
    for iata_code, full_name in  db.session.query(E.flown_airline, Airlines.full_name).\
            filter(E.credit_airline != credited).\
            join(Airlines, E.flown_airline==Airlines.iata_code).\
            distinct().all():
        other_airlines.append((iata_code, full_name))
    return jsonify({'partner airlines' : partner_airlines, 'other airlines' : other_airlines})

@app.route('/data/airports.json')
def airports():
    #return jsonify(utils.get_airports())
    return jsonify(["LAX", "Los Angeles"])

@app.route('/data/fare-codes/<flown>')
def fare_codes(flown):
    return jsonify({'codes': utils.get_fare_codes(airline=flown)})

@app.route('/data/flight-types/<flown>/<credited>')
def flight_types(flown, credited):
    return jsonify({'flight types' : utils.get_flight_type(flown_airline=flown, credit_airline=credited)})