from flask import Flask, render_template,url_for, redirect,flash
from flaskapp import app ,db
from flaskapp.models import cardioData
from flaskapp.forms import cardioForm
import numpy as np
from flaskapp.prediction import model

@app.route("/", methods=['GET', 'POST'])
def home():
    form = cardioForm()
    if form.validate_on_submit():
        data = cardioData(name=form.name.data,age=form.age.data,height=form.height.data,weight=form.weight.data,gender=form.gender.data,systolic=form.s_blood_pressure.data,diastolic=form.d_blood_pressure.data,cholestrol=form.cholestrol.data,glucose=form.glucose.data,alcohol=form.alcohol.data,smoking=form.smoking.data,physical=form.physical.data,disease=form.smoking.data)
        db.session.add(data)
        db.session.commit()
        users=cardioData.query.all()
        return redirect(url_for('result'))
    return render_template('home.html',form=form)


@app.route("/result",methods=['GET','POST'])
def result():
    users=cardioData.query.all()
    user=users[-1]
    arr = np.array([[user.gender,user.height,user.weight,user.systolic,user.diastolic,user.cholestrol,user.glucose,user.smoking,user.alcohol,user.physical,user.age]])
    stat=model.predict(arr)
    return render_template('result.html',stat=stat)