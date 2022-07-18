import os, subprocess
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

print(__name__)
app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=1440)
print(app.secret_key, app.config)

db =SQLAlchemy(app)

from app import routes