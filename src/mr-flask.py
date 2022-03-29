from flask import Flask, redirect, render_template, request, url_for, session, flash

from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        flash(f"Successfully logged in as {user}.")
        return redirect(url_for('userhome'))
    else:
        if 'user' in session:
            user = session['user']
            flash(f"Logged in as {user}.")
            return redirect(url_for('userhome'))
        return render_template('login.html')

@app.route('/userhome') 
def userhome():
    if 'user' in session:
        user = session['user']
        return render_template('userhome.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f"You have been logged out, {user}.", "info")
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

