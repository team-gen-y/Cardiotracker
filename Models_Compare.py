import numpy as np
import pandas as pd
import seaborn as sns

from sklearn import preprocessing
from sklearn.metrics import make_scorer, f1_score, recall_score, precision_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import log_loss

df = pd.read_csv('~/cardio_train.csv', sep = ';')

#Plotting to see how much of an impact the categorical variables have on the output classes
df_analysis = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc', 'smoke', 'alco', 'active'])

sns.catplot(x="variable", hue="value", col="cardio",
                data=df_analysis, kind="count", palette="Set1")



df.duplicated().values.any()
df.isnull().values.any()

df.describe()

# Removing outliers in height and weight
# I assumed the outliers to be <2 percentile and >98 percentile
df.drop(df[(df['height'] > df['height'].quantile(0.98)) | (df['height'] < df['height'].quantile(0.020))].index,inplace=True)
df.drop(df[(df['weight'] > df['weight'].quantile(0.98)) | (df['weight'] < df['weight'].quantile(0.020))].index,inplace=True)

#Diastolic blood pressure cannot be higher than systolic bp, so removing those that are higher
df[df['ap_lo']> df['ap_hi']]



#There were some negative values of both bp's which is not possible
#First I thought, it was probably a mistake and taking the absolute value should fix it
#df['ap_hi'] = df['ap_hi'].apply(lambda x : abs(x) if x < 0 else x)
#df['ap_lo'] = df['ap_lo'].apply(lambda x : abs(x) if x < 0 else x)



#Instead I decided to remove them altogether
df.drop(df[(df['ap_hi'] > df['ap_hi'].quantile(0.98)) | (df['ap_hi'] < df['ap_hi'].quantile(0.020))].index,inplace=True)
df.drop(df[(df['ap_lo'] > df['ap_lo'].quantile(0.98)) | (df['ap_lo'] < df['ap_lo'].quantile(0.020))].index,inplace=True)



blood_pressure = df.loc[:,['ap_lo','ap_hi']]
sns.boxplot(x = 'variable',y = 'value',data = blood_pressure.melt())
print("Diastilic pressure is higher than systolic one in {0} cases".format(df[df['ap_lo']> df['ap_hi']].shape[0]))



df.drop("id",axis=1,inplace=True)
df.drop_duplicates(inplace=True)
df['years'] = (df['age'] / 365).round(0)
df['years'] = pd.to_numeric(df['years'], downcast = 'integer')
df['Cardio'] = df['cardio']
df = df.drop('age', axis = 1)
df = df.drop('cardio', axis = 1)

#Plotting the correlation matrix
correlation_mat = df.corr()
top_corr_features = correlation_mat.index
plt.figure(figsize=(13,13))

g = sns.heatmap(df[top_corr_features].corr(), annot=True,cmap='RdYlGn')

#I tried to remove the features that were negatively impacting the model using the correlation matrix
#But some made the accuracy go down
#Removing alcohol made it go up by a slight amount
df=df.drop(['alco'], axis=1)

X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values



from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 1)


#Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter = 4000)
model.fit(X_train, Y_train)

y_preds = model.predict(X_test)
print(accuracy_score(Y_test, y_preds))

#Confusion Matrix
y_preds = model.predict(X_test)
print('Logistic Regression accuracy: ',accuracy_score(Y_test, y_preds))
print('\n')
import pylab as plt
labels=[0,1]
cmx=confusion_matrix(Y_test,y_preds, labels)
print(cmx)
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cmx)
plt.title('Confusion matrix of the classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
print('\n')
print(classification_report(Y_test, y_preds))



#Gradient Boost
from sklearn.ensemble import GradientBoostingClassifier

Grad_Boost = GradientBoostingClassifier(n_estimators=500, learning_rate=1, max_depth=1, verbose = True)
Grad_Boost.fit(X_train,Y_train)
Grad_Boost.score(X_test, Y_test)

y_preds = Grad_Boost.predict(X_test)
print('Gradient Boosting accuracy: ',accuracy_score(Y_test, y_preds))
print('\n')
import pylab as plt
labels=[0,1]
cmx=confusion_matrix(Y_test,y_preds, labels)
print(cmx)
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cmx)
plt.title('Confusion matrix of the classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
print('\n')
print(classification_report(Y_test, y_preds))


#ExtremeGradientBoosting - best accuracy so far in any model
import xgboost as xgb

XGB_Classifier = xgb.XGBClassifier(max_depth=12,
                        subsample=0.33,
                        objective='binary:logistic',
                        n_estimators=400,
                        learning_rate = 0.0001)
eval_set = [(X_train, Y_train), (X_test, Y_test)]
XGB_Classifier.fit(X_train, Y_train.ravel(), early_stopping_rounds=5, eval_metric=["error", "logloss"], eval_set=eval_set, verbose=True)



XGB_Classifier.score(X_test,Y_test)

y_preds = XGB_Classifier.predict(X_test)
print('XGB accuracy: ',accuracy_score(Y_test, y_preds))
print('\n')
import pylab as plt
labels=[0,1]
cmx=confusion_matrix(Y_test,y_preds, labels)
print(cmx)
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cmx)
plt.title('Confusion matrix of the classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
print('\n')
print(classification_report(Y_test, y_preds))


#AdaptiveBoost Classifier
from sklearn.ensemble import AdaBoostClassifier

AdaBoost_classifier = AdaBoostClassifier(n_estimators=500)
AdaBoost_classifier.fit(X_train,Y_train)
AdaBoost_classifier.score(X_test, Y_test)


#Bagging Classifer
from sklearn.ensemble import BaggingClassifier

Bag = BaggingClassifier(max_samples=0.5, max_features=1.0, n_estimators=50)
Bag.fit(X_train,Y_train)
Bag.score(X_test, Y_test)

#Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB

NB = MultinomialNB()
NB.fit(X_train,Y_train)
NB.score(X_test, Y_test)


#Simple Decision Tree
from sklearn.tree import DecisionTreeClassifier

DT = DecisionTreeClassifier(criterion="gini", random_state=50, max_depth=3, min_samples_leaf=5)
DT.fit(X_train,Y_train)
DT.score(X_test, Y_test)

#Random Forest
from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier()
RF.fit(X_train,Y_train)
RF.score(X_test, Y_test)
