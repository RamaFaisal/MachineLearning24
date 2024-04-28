import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
data = pd.read_csv("train.csv")
print(data.head())

x = data.iloc[:, 0:20]
y = data.iloc[:, -1]

bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(x,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(x.columns)

featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']
print(featureScores.nlargest(10,'Score'))

## Feature Importance
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

# Memuat data
data = pd.read_csv("train.csv")
x = data.iloc[:, 0:20] # independent columns
y = data.iloc[:, -1] #target column i.3 price

# Melakukan ExtraTreesClassifier unutk mengekekstraksi fitur
model = ExtraTreesClassifier()
model.fit(x, y)
print(model.feature_importances_) # use inbuilt class feature_importances of tree based classifiers

# Melakukan plot dari feature importances
feat_importances = pd.Series(model.feature_importances_, index = x.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()

## Matriks Korelasi dengan Heatmap
import seaborn as sns

# Memuat data
data = pd.read_csv("train.csv")
x = data.iloc[:,0:20] # independent columns
y = data.iloc[:, -1] # target column i.e price range
# Mendapatkan correlations dari setiap fitur dalam dataset
corrmat = data.corr()
top_corr_features = corrmat.index

## Lanjutan Heatmap
plt.figure(figsize=(20,20))
g = sns.heatmap(data[top_corr_features].corr(), annot=True, cmap="RdYlGn")
plt.show()