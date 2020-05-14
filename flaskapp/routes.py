from flask import Flask, render_template,url_for, redirect,flash, request
from flaskapp import app ,db
from flaskapp.models import cardioData,User
from flaskapp.forms import cardioForm,LoginForm,RegistrationForm
from flaskapp.newsfeed import allheadlines
import numpy as np
from flaskapp.cardiobot_predict import chatbot_response
from flaskapp.prediction import model
from flask_login import login_user, current_user,logout_user, login_required

@app.route('/')
def home():
    return render_template('actualhome.html')

@app.route('/process',methods=['POST'])
def process():
	user_input=request.form['user_input']

	bot_response=chatbot_response(user_input)
	print("Friend: "+bot_response)
	return render_template('chatbot.html',user_input=user_input,
		bot_response=bot_response)

@app.route('/chatbot',methods=['GET','POST'])
def chatbot():
    return render_template('chatbot.html')

@app.route("/test", methods=['GET', 'POST'])
def test():
    form = cardioForm()
    login=LoginForm()
    if form.validate_on_submit():
        data = cardioData(name=form.name.data,age=form.age.data,height=form.height.data,weight=form.weight.data,gender=form.gender.data,systolic=form.s_blood_pressure.data,diastolic=form.d_blood_pressure.data,cholestrol=form.cholestrol.data,glucose=form.glucose.data,alcohol=form.alcohol.data,smoking=form.smoking.data,physical=form.physical.data,disease=form.smoking.data)
        db.session.add(data)
        db.session.commit()
        users=cardioData.query.all()
        return redirect(url_for('result'))
    return render_template('home.html',form=form,login=login)


@app.route("/result",methods=['GET','POST'])
def result():
    users=cardioData.query.all()
    user=users[-1]
    arr = np.array([[user.gender,user.height,user.weight,user.systolic,user.diastolic,user.cholestrol,user.glucose,user.smoking,user.alcohol,user.physical,user.age]])
    stat=model.predict(arr)
    return render_template('result.html',stat=stat)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and (user.password==form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html')


@app.route('/newsfeed')
@login_required
def newsfeed():
    return render_template('newsfeed.html',allheadlines=allheadlines)