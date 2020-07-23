import csv
from flaskapp.clear import clear
from flask import Flask, render_template,url_for, redirect,flash, request
from flaskapp import app ,db
from flaskapp.models import cardioData,User, graphData
from flaskapp.forms import cardioForm,LoginForm,RegistrationForm,graphForm
from flaskapp.newsfeed import allheadlines
import numpy as np
from flaskapp.visuals import smokeperday,bpdisp,alcoperday,activtime,bminweight
import pandas as pd
from flaskapp.cardiobot_predict import chatbot_response
from flaskapp.prediction import Predict,Risk
from flask_login import login_user, current_user,logout_user, login_required
from flaskapp.visuals_2 import BP_display,Smoke_Display,Activity_Display,Alcohol_Display,Pulse_Display,BMI_Display
from flask import request

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

@app.route('/endpoint',methods=['GET','POST'])
def endpoint():
    user_input = request.args.get('input')
    return {
        'response': chatbot_response(user_input)
    }

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
    arr = np.array([[user.gender,user.height,user.weight,user.systolic,user.diastolic,user.cholestrol,user.glucose,user.smoking,user.alcohol,user.physical,user.age,user.disease]])
    stat=Predict(arr)
    risk=Risk(arr)
    return render_template('result.html',stat=stat,risk=risk)

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

@app.route('/charts')
@login_required
def charts():
    return render_template('charts.html')

@app.route('/account')
@login_required
def account():
    return render_template('account.html')


@app.route('/newsfeed')
@login_required
def newsfeed():
    return render_template('newsfeed.html',allheadlines=allheadlines)

@app.route('/userform', methods=['GET', 'POST'])
@login_required
def userform():
    form = graphForm()
    if form.validate_on_submit():
        flash(f'Data entered!', 'success')    
        graphEntry = graphData(age=form.age.data,gender=form.gender.data,height=form.height.data,weight=form.weight.data,bmi=form.bmi.data,ap_lo=form.s_blood_pressure.data,ap_hi=form.d_blood_pressure.data,pulse=form.pulse.data,num_smoke=form.smoke.data,num_alco=form.alcohol.data,activ_time=form.activity.data,user_id=current_user.id)
        db.session.add(graphEntry)
        db.session.commit()
        with open('flaskapp/user_data.csv','a',newline='') as file:
            writer = csv.writer(file)
            #writer.writerow(['age','gender','height','weight','bmi','ap_lo','ap_hi','pulse','num_smoke','num_alco','activ_time','date'])
            array = current_user.entry
            for entry in array:
                 writer.writerow([entry.age,entry.gender,entry.height,entry.weight,entry.bmi,entry.ap_lo,entry.ap_hi,entry.pulse,entry.num_smoke,entry.num_alco,entry.activ_time,entry.date])
        df = pd.read_csv('flaskapp/user_data.csv')
        #from flaskapp.visuals_2 import BP_display,Smoke_Display,Activity_Display,Alcohol_Display,Pulse_Display,BMI_Display
        Smoke_Display(df)
        Activity_Display(df)
        Alcohol_Display(df)
        Pulse_Display(df)
        BMI_Display(df)
        BP_display(df)
        clear()
        return redirect(url_for('charts'))
    return render_template('userform.html',form=form,current_user=current_user)