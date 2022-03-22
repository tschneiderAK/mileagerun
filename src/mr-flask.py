from time import time
from flask import Flask, redirect, render_template, request, url_for, session

from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for('userhome'))
    else:
        if 'user' in session:
            return redirect(url_for('userhome'))
        return render_template('login.html')

@app.route('/userhome') 
def userhome():
    if 'user' in session:
        user = session['user']
        return render_template('userhome.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    return "logout"
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

