from flask import Flask, render_template,url_for, redirect
from flaskapp import app
from flaskapp.models import cardioData
from flaskapp.forms import cardioForm


@app.route("/",methods=['GET','POST'])
def dataentry():
    form = cardioForm()
    if form.validate_on_submit():
        return redirect(url_for('result'))
    return render_template('form.html',form=form)

@app.route("/result",methods=['GET','POST'])
def result():
    return render_template('result.html')