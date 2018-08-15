import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
dataset = pd.read_csv('dataset.csv')
dataset = dataset.astype(float)
state = np.random.randint(100)
X = dataset.drop('clean',axis =	1)
y = dataset['clean']
print dataset.dtypes
X = np.asarray(X)
y = np.asarray(y)
X = X[:,1:]
#Random forest
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.15,random_state=0)
# clf1 = RandomForestClassifier()
# clf1.fit(X_train,y_train)
# y_pred=clf1.predict(X_test)
# tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
# accuracy = clf1.score(X_test,y_test)
# with open('randomforest.pickle','wb') as f:
#     pickle.dump(clf1, f)
#multilayer perceptron
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.15,random_state = 0)
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
mlp = MLPClassifier(hidden_layer_sizes=(15,15,15,15,15,15))
mlp.fit(X_train,y_train)
predictions = mlp.predict(X_test)
tn, fp, fn, tp = confusion_matrix(y_test, predictions).ravel()
accuracy = mlp.score(X_test,y_test)
with open('multilayerperceptron.pickle','wb') as f:
    pickle.dump(mlp, f)
print "TN = ",tn
print "TP = ",tp
print "FP = ",fp
print "FN = ",fn
print accuracy
