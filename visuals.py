import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px

def read(df):
    df = pd.read_csv('user_data.csv')
    return df

#3D display of blood pressures
def BP_display(df):
    DF = df
    DF['bp_cat'] = ""

    for i in range(len(DF)):
        if DF.ap_lo[i]<=60 and DF.ap_hi[i]<=100:
            DF.bp_cat[i] = 'low'
        elif (DF.ap_lo[i]>60 and DF.ap_lo[i]<=80) or (DF.ap_hi[i]>100 and DF.ap_hi[i]<=120):
            DF.bp_cat[i] = 'normal'
        elif (DF.ap_lo[i]>80) or (DF.ap_hi[i]>120):
            DF.bp_cat[i] = 'high'

    DF['bp_sum'] = ""

    for i in range(len(DF)):
        DF.bp_sum[i] = float(0.25 * (DF.ap_lo[i] + DF.ap_hi[i]))
    DF.bp_sum = pd.to_numeric(DF.bp_sum)
    
    fig = px.scatter_3d(DF, x = 'ap_lo', y = 'ap_hi', z = 'date', color = 'bp_cat', size = 'bp_sum', size_max = 100, hover_name = 'bp_cat')
    pio.show(fig)

#Scatter Display of pulse rates
def Pulse_Display(df):
    fig = px.scatter(df, x="date", y="pulse", size = 'pulse', size_max = 60)
    fig.show()

#Scatter Display of BMI with hovering weights
def BMI_Display(df):
    DF = df
    DF['bmi_cat'] = ""

    for i in range(len(DF)):
        if DF.bmi[i] < 18.5:
            DF.bmi_cat[i] = 'underweight'
        elif DF.bmi[i] >= 18.5 and DF.bmi[i] <= 24.9:
            DF.bmi_cat[i] = 'healthy weight'
        else:
            DF.bmi_cat[i] = 'obese'

    fig = px.scatter(DF, x = 'date', y = 'bmi', color = 'bmi_cat', size = 'bmi', size_max = 60, hover_name = 'weight')
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

#clear csv
def clear_all(df):
    df = df[0:0]
    df = df.to_csv('user_data.csv', index = False)


########## ALL FUNCTOINS ##############
#Read CSV
df = None
df = read(df)
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
#clear csv
clear_all(df)
