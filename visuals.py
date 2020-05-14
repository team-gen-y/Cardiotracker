#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as mp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('user_data.csv')

def smokeperday(ID, df):
    data = df.loc[df.id == ID]
    plt.plot(data.date, data.num_smoke, color = 'brown')
    plt.xticks(rotation = 90)
    plt.xlabel('date')
    plt.ylabel('number of cigarettes')
    plt.grid()
    plt.show()
    #g = sns.lineplot(x = data.date, y = data.num_smoke, color = 'brown').set_xticklabels(df.date, rotation = 90)
    
def bpdisp(ID, df):
    data = df.loc[df.id == ID]
    plt.plot(data.date, data.ap_lo, color = 'yellow', label = 'diastolic')
    plt.plot(data.date, data.ap_hi, color = 'blue', label= 'systolic')
    plt.legend(loc="upper right")
    plt.xticks(rotation = 90)
    plt.xlabel('date')
    plt.ylabel('blood pressure')
    plt.grid()
    plt.show()
    #sns.lineplot(x = data.date, y = data.ap_lo, color = 'blue').set_xticklabels(df.date, rotation = 90)
    #sns.lineplot(x = data.date, y = data.ap_hi, color = 'yellow').set_xticklabels(df.date, rotation = 90)
    
def bp_lo(ID, df):
	data = df.loc[df.id == ID]
	plt.plot(data.date, data.ap_lo, color = 'yellow')
	plt.xticks(rotation = 90)
	plt.xlabel('date')
	plt.ylabel('BP')
	plt.grid()
	plt.show()
	
def bp_hi(ID, df):
	data = df.loc[df.id == ID]
	plt.plot(data.date, data.ap_hi, color = 'blue')
	plt.xticks(rotation = 90)
	plt.xlabel('date')
	plt.ylabel('BP')
	plt.grid()
	plt.show()

def alcoperday(ID, df):
    data = df.loc[df.id == ID]
    plt.plot(data.date, data.num_alco, color = 'red')
    plt.xticks(rotation = 90)
    plt.xlabel('date')
    plt.ylabel('liters of alcohol consumed')
    plt.grid()
    plt.show()
    
def activtime(ID, df):
    data = df.loc[df.id == ID]
    plt.plot(data.date, data.activ_time, color = 'green')
    plt.xticks(rotation = 90)
    plt.xlabel('date')
    plt.ylabel('hours of physical activity')
    plt.grid()
    plt.show()
    
def bminweight(ID, df):
    data = df.loc[df.id == ID]
    plt.plot(data.date, data.bmi, color = 'black', label = 'bmi')
    plt.plot(data.date, data.weight, color = 'purple', label= 'weight')
    plt.legend(loc="upper right")
    plt.xticks(rotation = 90)
    plt.xlabel('date')
    plt.ylabel('blood pressure')
    plt.grid()
    plt.show()
    
#smokeperday() #put parameters customer_id and 'df'
bpdisp() #put parameters customer_id and 'df'
bp_lo()
bp_hi()
#alcoperday() #put parameters customer_id and 'df'
#activtime() #put parameters customer_id and 'df'
bminweight() #put parameters customer_id and 'df'

