from datetime import timedelta
import os

import yaml

from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

spec = APISpec(
    title="MileageRun",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin()],
)

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=1440)

db =SQLAlchemy(app)

from app import routes