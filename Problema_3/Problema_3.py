from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report
import matplotlib.gridspec as gridspec
from sklearn.decomposition import PCA
from mlxtend.plotting import plot_decision_regions
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
data = pd.read_csv('Dados_geladeira.csv')
x = data.drop('Estado', axis=1)
y = data['Estado']
X_Train,X_Test,Y_Train,Y_Test=train_test_split(x, y, test_size=.3, random_state=20)
modeltree = DecisionTreeClassifier()
pca = PCA(n_components = 2)
X_train2 = pca.fit_transform(X_Train)
X_Test2 = pca.fit_transform(X_Test)
modeltree.fit(X_train2, Y_Train)
print(modeltree.score(X_train2,Y_Train))
print(modeltree.score(X_Test2,Y_Test))
ytr = Y_Train.to_numpy()
yte = Y_Test.to_numpy()
fig = plt.figure(figsize=(10,8))
gs = gridspec.GridSpec(2, 2)
plot_decision_regions(X=X_train2,
                      y=ytr,
                      clf=modeltree,
                      legend=2)
plt.title("Decision Tree Geladeira Treino")
plt.show()

plt.title("Decision Tree Geladeira teste")
plot_decision_regions(X=X_Test2,
                      y=yte,
                      clf=modeltree,
                      legend=2)
plt.show()






'''
modelknn = KNeighborsClassifier(n_neighbors=3)
modellr = LogisticRegression()
modelknn.fit(X_Train,Y_Train)
modellr.fit(X_Train,Y_Train)
tree = modeltree.fit(X_Train,Y_Train)
modeltree.fit(X_Train,Y_Train)
predknn = modelknn.predict(X_Test)
predlr = modellr.predict(X_Test)
predtree = modeltree.predict(X_Test)
print(classification_report(Y_Test,predknn))
print(classification_report(Y_Test,predlr))
print(classification_report(Y_Test,predtree))
print(modelknn.score(X_Train,Y_Train))
print(modelknn.score(X_Test,Y_Test))
print(modellr.score(X_Train,Y_Train))
print(modellr.score(X_Test,Y_Test))
predicoes = []
predicoes.append(modeltree.predict(pd.DataFrame({'Tensão':230,'Corrente':1.22,'Rotação':4200,'Eficiencia':4.88,'Potência':89.6}, index=[0])))
predicoes.append(modeltree.predict(pd.DataFrame({'Tensão':230,'Corrente':1.05,'Rotação':6000,'Eficiencia':5.27,'Potência':82.6}, index=[0])))
predicoes.append(modeltree.predict(pd.DataFrame({'Tensão':230,'Corrente':1.05,'Rotação':3600,'Eficiencia':3.02,'Potência':82.4}, index=[0])))
predicoes.append(modeltree.predict(pd.DataFrame({'Tensão':230,'Corrente':1.05,'Rotação':4500,'Eficiencia':5.15,'Potência':100.4}, index=[0])))
predicoes.append(modeltree.predict(pd.DataFrame({'Tensão':130,'Corrente':1.05,'Rotação':2200,'Eficiencia':5.23,'Potência':82.8}, index=[0])))
print(predicoes)
'''