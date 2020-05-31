import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px

df = pd.read_csv('user_data.csv')

df['bp_cat'] = ""

for i in range(len(df)):
    if df.ap_lo[i]<=60 and df.ap_hi[i]<=100:
        df.bp_cat[i] = 'low'
    elif (df.ap_lo[i]>60 and df.ap_lo[i]<=80) or (df.ap_hi[i]>100 and df.ap_hi[i]<=120):
        df.bp_cat[i] = 'normal'
    elif (df.ap_lo[i]>80) or (df.ap_hi[i]>120):
        df.bp_cat[i] = 'high'

df['bmi_cat'] = ""

for i in range(len(df)):
    if df.bmi[i] < 18.5:
        df.bmi_cat[i] = 'underweight'
    elif df.bmi[i] >= 18.5 and df.bmi[i] <= 24.9:
        df.bmi_cat[i] = 'healthy weight'
    else:
        df.bmi_cat[i] = 'obese'

df['bp_sum'] = ""

for i in range(len(df)):
    df.bp_sum[i] = float(0.25 * (df.ap_lo[i] + df.ap_hi[i]))
    
df.bp_sum = pd.to_numeric(df.bp_sum)

#empty the csv file
def clear_all():
    global df
    df = df.drop(['bp_cat', 'bmi_cat', 'bp_sum'], axis = 1)
    df = df[0:0]
    df.to_csv('user_data.csv')


#3D display of blood pressures
def BP_display(df):
    trace1 = go.Scatter3d(
        x=df.ap_lo,
        y=df.ap_hi,
        z=df.date,
        mode='markers',
        marker=dict(
            size=10,
            color='rgb(255,0,0)',    # set color to an array/list of desired values      
        )
    )

    data = [trace1]
    layout = go.Layout(
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0  
        )
    
    )  
    fig = go.Figure(data=data, layout=layout)
    fig = px.scatter_3d(df, x = 'ap_lo', y = 'ap_hi', z = 'date', color = 'bp_cat', size = 'bp_sum', size_max = 100, hover_name = 'bp_cat')
    pio.show(fig)

#Scatter Display of pulse rates
def Pulse_Display(df):
    fig = px.scatter(df, x="date", y="pulse", size = 'pulse', size_max = 60)
    fig.show()

#Scatter Display of BMI with hovering weights
def BMI_Display(df):
    fig = px.scatter(df, x = 'date', y = 'bmi', color = 'bmi_cat', size = 'bmi', size_max = 60, hover_name = 'weight')
    fig.show()

#Linear Display of smokes per day
def Smoke_Display(df):
    fig = px.line(df, x = 'date', y = 'num_smoke')
    fig.show()

#Linear Display of alcohol per day
def Alcohol_Display(df):
    fig = px.line(df, x = 'date', y = 'num_alco')
    fig.show()

#Linear Display of active time per day
def Activity_Display(df):
    fig = px.line(df, x = 'date', y = 'active_time')
    fig.show()

########## ALL FUNCTOINS ##############
#3D display of blood pressures
BP_display(df)
#Scatter Display of pulse rates
Pulse_Display(df)
#Scatter Display of BMI with hovering weights
BMI_Display(df)
#Linear Display of smokes per day
Smoke_Display(df)
#Linear Display of alcohol per day
Alcohol_Display(df)
#Linear Display of active time per day
Activity_Display(df)
