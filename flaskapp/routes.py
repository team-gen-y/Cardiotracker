from flask import Flask, render_template,url_for, redirect,flash
from flaskapp import app ,db
from flaskapp.models import cardioData
from flaskapp.forms import cardioForm


@app.route("/", methods=['GET', 'POST'])
def home():
    form = cardioForm()
    if form.validate_on_submit():
        i=0
        data = cardioData(name=form.name.data,age=form.age.data,height=form.height.data,weight=form.weight.data,gender=form.gender.data,systolic=form.s_blood_pressure.data,diastolic=form.d_blood_pressure.data,cholestrol=form.cholestrol.data,glucose=form.glucose.data,alcohol=form.alcohol.data,smoking=form.smoking.data,physical=form.physical.data,disease=form.smoking.data)
        db.session.add(data)
        db.session.commit()
        users=cardioData.query.all()
        flash(f'Account created for {users[-1]}!', 'success')
        return redirect(url_for('result'))
    return render_template('home.html',form=form)


@app.route("/result",methods=['GET','POST'])
def result():
    return render_template('result.html')