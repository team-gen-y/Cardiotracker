#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import seaborn as sns


df = pd.read_csv('cardio_train.csv', sep = ';')
df.drop("id",axis=1,inplace=True)
df.drop_duplicates(inplace=True)
df['years'] = (df['age'] / 365).round(0)
df['years'] = pd.to_numeric(df['years'], downcast = 'integer')
df['Cardio'] = df['cardio']
df = df.drop('age', axis = 1)
df = df.drop('cardio', axis = 1)

X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 1)

from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 1)
forest.fit(X_train, Y_train)
model = forest

#model.predict(np.array)

