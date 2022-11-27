# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TayD_3tbnP6ZGPxBjLDlgpbO7dy2wG_8
"""

# Commented out IPython magic to ensure Python compatibility.
# jhony alejandro herrera parrado 
#En primer lugar importamos los archivos necesario para el programa y la base de datos tomada de  https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009 y los
from sklearn.metrics import matthews_corrcoef 
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from subprocess import check_output
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve,roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn import decomposition 
# %matplotlib inline
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
import lightgbm as lgb
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler 
from sklearn import datasets
from sklearn.decomposition import PCA, KernelPCA
from sklearn.datasets import make_circles, make_moons, make_classification
from sklearn.metrics import matthews_corrcoef

rdwineq = pd.read_csv('/content/winequality-red.csv')  # cargar dataset
rdwineq.head(-1)  # cabecera de primeros  y ultimos datos del dataset

# proceso de eliminación y ajustes de valores NAN  en  cada caracteristica
rdwineq['fixed acidity'].fillna(rdwineq['fixed acidity'].mean(),inplace=True) # acidez fija
rdwineq['volatile acidity'].fillna(rdwineq['volatile acidity'].mean(),inplace=True) #acidez volátil
rdwineq['residual sugar'].fillna(rdwineq['residual sugar'].mean(), inplace=True) #ácido cítrico
rdwineq['citric acid'].fillna(rdwineq['citric acid'].mean(),inplace=True) #azúcar residual
rdwineq['chlorides'].fillna(rdwineq['chlorides'].mean(), inplace=True) #cloruros
rdwineq['free sulfur dioxide'].fillna(rdwineq['free sulfur dioxide'].mean(),inplace=True)#dióxido de azufre libre
rdwineq['total sulfur dioxide'].fillna(rdwineq['total sulfur dioxide'].mean(),inplace=True) #dióxido de azufre total
rdwineq['density'].fillna(rdwineq['density'].mean(), inplace=True) #densidad
rdwineq['pH'].fillna(rdwineq['pH'].mean(), inplace=True) #pH
rdwineq['sulphates'].fillna(rdwineq['sulphates'].mean(),inplace=True)#sulfatos
rdwineq['alcohol'].fillna(rdwineq['alcohol'].mean(),inplace=True) # alcohol
rdwineq['quality'].fillna(rdwineq['quality'].mean(),inplace=True) #calidad

rdwineq.info(-1) # resumen de información

rdwineq.describe()  # cabecera de primeros  y ultimos datos del datase luego de los ajustes

fig = plt.figure(figsize = (8,8))
sns.barplot(x = 'quality', y = 'fixed acidity', data =rdwineq)  # aacidez fija

fig = plt.figure(figsize = (8,8))
sns.barplot(x = 'quality', y = 'volatile acidity', data =rdwineq) #acidez volátil

fig = plt.figure(figsize = (8,38))
sns.barplot(x = 'quality', y = 'citric acid', data = rdwineq) #ácido cítrico

fig = plt.figure(figsize = (8,8))
sns.barplot(x = 'quality', y = 'residual sugar', data = rdwineq)#azúcar residual

fig = plt.figure(figsize = (8,8))
sns.barplot(x = 'quality', y = 'chlorides', data =rdwineq)#libre de cloruros

fig = plt.figure(figsize = (8,8))
sns.barplot(x = 'quality', y = 'free sulfur dioxide', data = rdwineq)#dioxido sulfuroso

fig = plt.figure(figsize = (8,8))
sns.barplot(x = 'quality', y = 'total sulfur dioxide', data =rdwineq)# dióxido de azufre libre

fig = plt.figure(figsize = (8,8))
sns.barplot(x = 'quality', y = 'sulphates', data =rdwineq) # % de sulfatos

fig = plt.figure(figsize = (8,8))
sns.barplot(x = 'quality', y = 'alcohol', data = rdwineq) # % alcohol

fig = plt.figure(figsize = (8,8))
sns.barplot(x = 'quality', y = 'pH', data =rdwineq) # % de pH

y=rdwineq['quality'] # se dividen los datos en  Y y X
y

x=rdwineq.drop(columns=['quality'], axis=1) # se dividen los datos en  Y y X
x

dato2=pd.concat([x,y], axis=1) # se concatenan  de  nuevo
dato2

dato2.to_csv('datos2_data.csv', index=False) # se  exporta el archivo con los nuevos datos

X_train1, X_validate, Y_train1, Y_validate = train_test_split(x,y, test_size=0.1, random_state=2) #   ahora se usan los datos de forma que 70 % de los datos para se usan entrenar, 20 % para probar y el 10 % para validar el método
X_train, X_test, Y_train, Y_test = train_test_split(X_train1,Y_train1, test_size=0.2222, random_state=2)

scaler = StandardScaler() # se estandarizan los datos
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)  
X_validate = scaler.transform(X_validate)

fig =plt.figure(2,figsize=(8, 8))
n=6
pca=decomposition.PCA(n_components=n)
pca.fit(X_train)
X_train=pca.transform(X_train)
Y_train=np.choose(Y_train, [1,2,3,4,5,6,7,8,9,10,0]).astype(float)
plt.scatter(X_train[:, 0], X_train[:, 1],  c=Y_train,)
plt.show()
print("  grafica de pca :",pca.explained_variance_ratio_)
#por el criterio del 97 % no hay necesidad de hacer una reduccion de dimensiones#

modelo_knn = KNeighborsClassifier().fit(X_train, Y_train)# se implementa modelo knn

# proceso de entrenemanieto
modelo_knn = KNeighborsClassifier().fit(X_train, Y_train) #modelo knn
params = { 'n_neighbors': range(1,50),
            'weights' : ["uniform","distance"],
            'metric' : ["euclidean","manhattan","chebyshev","minkowski"],
            'algorithm' : ["auto", "ball_tree", "kd_tree", "brute"]}
grid = GridSearchCV(estimator= KNeighborsClassifier(), param_grid=params, cv= 10)
grid_search=grid.fit(X_train, Y_train) #grid_search
print(grid_search.best_params_) #se imprime grid_search

accuracy = grid_search.best_score_ *100  #  se escoge el  mejor accuracy 
print("La precisión de nuestro conjunto de datos de entrenamiento con ajuste es: {:.2f}%".format(accuracy) )

#ahora se hace un reciclaje con los mejores parámetros y con el 90% de los datos que son  70 % de los datos para se usan entrenar, 20 % para probar
knn = KNeighborsClassifier(algorithm= 'auto', metric= 'chebyshev', n_neighbors= 31,metric_params=None, weights= 'distance')
knn.fit(X_train1, Y_train1)
y_test_hat=knn.predict(X_validate) 
test_accuracy=accuracy_score(Y_validate,y_test_hat)*100
print("La precisión de nuestro conjunto de datos de entrenamiento con ajuste es con el total de datos : {:.2f}%".format(test_accuracy) )
MCC = matthews_corrcoef(Y_validate, y_test_hat) # cofeciente de matthews
print("MCC = ", MCC)

paramdt = {'criterion' : ['gini','entropy'], #se hace DecisionTreeClassifier
              'max_depth': range(1,20),
              'min_samples_split': range(1,15),
              'min_samples_leaf': range(1,15)}
griddt = GridSearchCV(estimator= DecisionTreeClassifier(),param_grid=paramdt, cv= 10)
grid_searchdt=griddt.fit(X_train, Y_train) #grid_search
print(grid_searchdt.best_params_) # imprimir los dados

accuracydt = grid_searchdt.best_score_ *100
print("La precisión de nuestro conjunto de datos de entrenamiento con ajuste es : {:.2f}%".format(accuracydt) ) #

dt = DecisionTreeClassifier(criterion= 'entropy', max_depth= 19, min_samples_leaf= 1,min_samples_split= 2)
dt.fit(X_train1, Y_train1)
y_test_hat=dt.predict(X_validate) 
test_accuracy=accuracy_score(Y_validate,y_test_hat)*100
print("Accuracy for our testing dataset with tuning is : {:.2f}%".format(test_accuracy) )

MCC = matthews_corrcoef(Y_validate, y_test_hat)
print("MCC = ", MCC)