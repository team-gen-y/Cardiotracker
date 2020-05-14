from flask import Flask
from flaskapp.forms import cardioForm
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flaskapp.cardiobot_predict import chatbot_response

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from flaskapp import routes