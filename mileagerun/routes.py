
from flask import redirect, render_template, request, url_for, session, flash
from mileagerun.models import *
from mileagerun import app, db
from mileagerun.utils import miles_flown
from mileagerun.forms import *

@app.route('/', methods=['POST', 'GET'])
def home():
    form = SampleFlight()    
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
    if form.is_submitted():
        print('Form submitted')
        print(form.csrf_token)
    if form.validate_on_submit():
        print('valid')

    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        found_user =User.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = User(name=user, email=None)
            db.session.add(usr)
            db.session.commit()

        flash(f"Successfully logged in as {user}.")
        return redirect(url_for('userhome'))
    else:
        if 'user' in session:
            user = session['user']
            flash(f"Logged in as {user}.")
            return redirect(url_for('userhome'))
        return render_template('login.html')

@app.route('/userhome', methods=['POST', 'GET']) 
def userhome():
    email = None
    if 'user' in session:
        user = session['user']

        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            found_user = User.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash('Email saved')
        else:
            if 'email' in session:
                email = session['email']

        return render_template('userhome.html', email=email, user=user)
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