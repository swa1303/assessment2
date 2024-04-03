# -*- coding: utf-8 -*-
"""LVADSUSR125_SwathiM_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Z_1XcTKvpV-Y7QZOj1JQJmXwJHJsOU9
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, precision_score, f1_score, recall_score, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import time
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("https://raw.githubusercontent.com/Deepsphere-AI/LVA-Batch4-Assessment/main/auto-mpg.csv")

data.head()

data.info()

data.shape

data.isna().sum()

data.fillna(data.mean(), inplace=True)

data.isna().sum()

data['horsepower'] = data['horsepower'].replace('?', np.nan)

data['horsepower'] = pd.to_numeric(data['horsepower'], errors='coerce')

data['horsepower'].fillna(data['horsepower'].mean(), inplace=True)

data.isna().sum()

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1

outliers = ((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)
print(outliers)

df = data[~outliers]

df.shape

df.drop(columns=['car name'], inplace=True)

print(df.describe())

sns.histplot(df['mpg'], kde=True)
plt.title('Distribution of Fuel Efficiency (mpg)')
plt.xlabel('mpg')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12, 6))
numerical_cols = ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']
for i, col in enumerate(numerical_cols, 1):
    plt.subplot(2, 3, i)
    sns.scatterplot(x=col, y='mpg', data=df)
    plt.title(f'{col} vs. mpg')
plt.tight_layout()
plt.show()

X = df.drop(columns=['mpg'])
y = df['mpg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))