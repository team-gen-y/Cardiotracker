import numpy as mp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('flaskapp/user_data.csv')

def smokeperday(df):
    data = df
    plt.plot(data.date, data.num_smoke, color = 'brown')
    plt.xticks(rotation = 90)
    plt.xlabel('date')
    plt.ylabel('number of cigarettes') 
    plt.grid()
    plt.savefig('flaskapp/static/images/plots/smoke_plot.png')
    plt.show()
    #g = sns.lineplot(x = data.date, y = data.num_smoke, color = 'brown').set_xticklabels(df.date, rotation = 90)

def bpdisp(df):
    data = df#.loc[df.id == ID]
    plt.plot(data.date, data.ap_lo, color = 'yellow', label = 'diastolic')
    plt.plot(data.date, data.ap_hi, color = 'blue', label= 'systolic')
    plt.legend(loc="upper right")
    plt.xticks(rotation = 90)
    plt.xlabel('date')
    plt.ylabel('blood pressure')
    plt.grid()
    plt.savefig('flaskapp/static/images/plots/bp_plot.png')
    plt.show()
    #sns.lineplot(x = data.date, y = data.ap_lo, color = 'blue').set_xticklabels(df.date, rotation = 90)
    #sns.lineplot(x = data.date, y = data.ap_hi, color = 'yellow').set_xticklabels(df.date, rotation = 90)

def alcoperday(df):
    data = df
    plt.plot(data.date, data.num_alco, color = 'red')
    plt.xticks(rotation = 90)
    plt.xlabel('date')
    plt.ylabel('liters of alcohol consumed')
    plt.grid()
    plt.savefig('flaskapp/static/images/plots/alc_plot.png')
    plt.show()

def activtime(df):
    data = df
    plt.plot(data.date, data.activ_time, color = 'green')
    plt.xticks(rotation = 90)
    plt.xlabel('date')
    plt.ylabel('hours of physical activity')
    plt.grid()
    plt.savefig('flaskapp/static/images/plots/activ_plot.png')
    plt.show()

def bminweight(df):
    data = df
    plt.plot(data.date, data.bmi, color = 'black', label = 'bmi')
    plt.plot(data.date, data.weight, color = 'purple', label= 'weight')
    plt.legend(loc="upper right")
    plt.xticks(rotation = 90)
    plt.xlabel('date')
    plt.ylabel('blood pressure')
    plt.grid()
    plt.savefig('flaskapp/static/images/plots/bmi_plot.png')
    plt.show()

