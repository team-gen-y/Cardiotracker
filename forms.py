from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email 

class cardioForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    height = IntegerField('Height',
                        validators=[DataRequired()])

    age = IntegerField('Age',
                        validators=[DataRequired()])
    gender = RadioField('Gender',
                        choices=[(1,'Male'),(0,'Female')],
                        validators=[DataRequired()])
    s_blood_pressure = IntegerField('Systolic blood pressure',
                        validators=[DataRequired()])
    d_blood_pressure = IntegerField('Diastolic blood pressure',
                        validators=[DataRequired()])
    cholestrol = SelectField('Cholestrol',
                        choices=[(1,'Normal'),(2,'Above normal'),(3,'Well above normal')],
                        validators=[DataRequired()])
    glucose = SelectField('Glucose',
                        choices=[(1,'Normal'),(2,'Above normal'),(3,'Well above normal')],
                        validators=[DataRequired()])
    smoking = SelectField('Smoking habit',
                        choices=[('Yes','Yes'),('No','No')])
    alcohol = SelectField('Alcohol intake',
                        choices=[(1,'Yes'),(0,'No')])
    physical = SelectField('Physical activity',
                        choices=[(1,'Yes'),(0,'No')])
    disease = SelectField('Presence of cardiovascular disease',
                        choices=[(1,'Yes'),(0,'No')])
