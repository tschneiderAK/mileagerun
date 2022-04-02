from flask import redirect, render_template, request, url_for, session, flash
from mileagerun.models import *
from mileagerun import app, db
from mileagerun.utils import miles_flown
from mileagerun.forms import *

@app.route('/', methods=['POST', 'GET'])
def home():
    form = SampleFlightForm()    
    form.validate_on_submit()
    if request.method == 'POST':
        distance = miles_flown.calc_distance(origin=form.origin.data, destination=form.destination.data)
        return render_template('index.html', distance=distance, form=form)
    return render_template('index.html', distance=0, form=form)

@app.route('/view')
def view():
    return render_template('view.html', values=User.query.all())

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        registration = User(first_name = form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            password=form.password.data)
        
        db.session.add(registration)
        db.session.commit()
        return redirect(url_for('login'), code=307)
        
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        user_password = User.query.filter_by(email=email).first().password
        if user_password == form.password.data:
            session.permanent = True
            session['email'] = email
            flash(f"Successfully logged in.")
            return redirect(url_for('userhome'))
        else:
            flash(f"Incorrect username or password.")
            return redirect(url_for('login', email=form.email.data)) 

    else:
        if 'user' in session:
            user = session['user']
            flash(f"Logged in as {user}.")
            return redirect(url_for('userhome'))
        return render_template('login.html', form=form)

@app.route('/userhome', methods=['POST', 'GET']) 
def userhome():
    if 'email' in session:
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
    values = db.session.query(earnings).all()
    return render_template('earnings.html', values=values)