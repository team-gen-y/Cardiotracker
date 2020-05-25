from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,RadioField, SelectField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired, Length, Email , EqualTo
class NonValidatingSelectField(SelectField):
    def pre_validate(self, form):
        pass
class NonValidatingRadioField(RadioField):
    def pre_validate(self, form):
        pass

class cardioForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    age = IntegerField('Age',
                        validators=[DataRequired()])
    height = IntegerField('Height',
                        validators=[DataRequired()])
    weight = IntegerField('Weight',
                        validators=[DataRequired()])
    gender = NonValidatingRadioField('Gender',
                        choices=[(1,'Male'),(2,'Female')],
                        validators=[DataRequired()])
    s_blood_pressure = IntegerField('Systolic blood pressure',
                        validators=[DataRequired()])
    d_blood_pressure = IntegerField('Diastolic blood pressure',
                        validators=[DataRequired()])
    cholestrol = NonValidatingSelectField('Cholestrol',
                        choices=[(1,'Normal'),(2,'Above normal'),(3,'Well above normal')],
                        validators=[DataRequired()])
    glucose = NonValidatingSelectField('Glucose',
                        choices=[(1,'Normal'),(2,'Above normal'),(3,'Well above normal')],
                        validators=[DataRequired()])
    smoking = NonValidatingSelectField('Smoking habit',
                        choices=[(1,'Yes'),(0,'No')])
    alcohol = NonValidatingSelectField('Alcohol intake',
                        choices=[(1,'Yes'),(0,'No')])
    physical = NonValidatingSelectField('Physical activity',
                        choices=[(1,'Yes'),(0,'No')])
    disease = NonValidatingSelectField('Presence of cardiovascular disease',
                        choices=[(1,'Yes'),(0,'No')])
    submit = SubmitField('View Result')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class graphForm(FlaskForm):
    age = IntegerField('Age',
                        validators=[DataRequired()])
    gender = NonValidatingRadioField('Gender',
                        choices=[(1,'Male'),(2,'Female')],
                        validators=[DataRequired()])
    height = IntegerField('Height',
                        validators=[DataRequired()])
    weight = IntegerField('Weight',
                        validators=[DataRequired()])
    bmi = IntegerField('Bmi',
                        validators=[DataRequired()])
    s_blood_pressure = IntegerField('Systolic blood pressure',
                        validators=[DataRequired()])
    d_blood_pressure = IntegerField('Diastolic blood pressure',
                        validators=[DataRequired()])
    pulse = IntegerField('Pulse',
                        validators=[DataRequired()])
    smoke = IntegerField('Cigarettes per day',
                        validators=[DataRequired()])
    alcohol = IntegerField('Alcohol intake per day',
                        validators=[DataRequired()])
    activity = IntegerField('Exercise per day in minutes',
                        validators=[DataRequired()])
    submit = SubmitField('Enter your details')