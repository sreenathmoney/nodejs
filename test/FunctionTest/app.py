from flask import Flask
from flask_cors import CORS
from datetime import timedelta
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import os


app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.secret_key = "Manish@DEV#01389asd80L"
jwt = JWTManager(app)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
CORS(app)