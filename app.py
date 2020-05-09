from flask import Flask, render_template,url_for
from forms import cardioForm
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY 

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/datainput")
def dataentry():
    form = cardioForm()
    return render_template('form.html',form=form)