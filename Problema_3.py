from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv('Dados_geladeira.csv')
x = data.drop('Estado', axis=1)
y = data['Estado']
X_Train,X_Test,Y_Train,Y_Test=train_test_split(x,y,test_size=.3)
modelknn = KNeighborsClassifier(n_neighbors=3)
modellr = LogisticRegression()
modeltree = DecisionTreeClassifier()
modelknn.fit(X_Train,Y_Train)
modellr.fit(X_Train,Y_Train)
modeltree.fit(X_Train,Y_Train)
predknn = modelknn.predict(X_Test)
predlr = modellr.predict(X_Test)
predtree = modeltree.predict(X_Test)
#print(classification_report(Y_Test,predknn))
#print(classification_report(Y_Test,predlr))
#print(classification_report(Y_Test,predtree))
print(modelknn.score(X_Train,Y_Train))
print(modelknn.score(X_Test,Y_Test))
print(modellr.score(X_Train,Y_Train))
print(modellr.score(X_Test,Y_Test))
print(modeltree.score(X_Train,Y_Train))
print(modeltree.score(X_Test,Y_Test))
#print(modeltree.predict(pd.DataFrame({'Tensão':230,'Corrente':1.22,'Rotação':4200,'Eficiencia':4.88,'Potência':89.6}, index=[0])))