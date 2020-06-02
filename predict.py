#libraries
import pandas as pd
import numpy as np

#reading csv
df = pd.read_csv('cardio_train.csv', sep = ';')

#organizing data
df['years'] = (df['age'] / 365).round(0)
df['years'] = pd.to_numeric(df['years'], downcast = 'integer')
df['Cardio'] = df['cardio']
df = df.drop('age', axis = 1)
df = df.drop('cardio', axis = 1)

#separating dataframe into input matrix and target vector
X = np.array(df.iloc[:, :-1].values, dtype = np.float128)
Y = df.iloc[:, -1].values

#splitting data intro training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 1)

#setting ML model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

#fitting the training data into the model
model.fit(X_train, Y_train)

#predicting the disease with given list
def Predict(lst):
    arr = np.array([lst])
    return model.predict(arr)[0]

#getting the risk % of having the disease with the given list
def Risk(lst):
    arr = np.array([lst])
    p =(model.predict_proba(arr))
    risk = round(p[0][1] * 100, 2)
    return risk

######   ALL FUNCTIONS ######
'''
Predict(lst) - 1 for yes, 0 for no
Risk(lst) - risk %
''' 