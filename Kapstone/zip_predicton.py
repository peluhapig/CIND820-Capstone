from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics
import pandas as pd


df = pd.read_csv('sample_zips.csv') #loading the dataset
df = df[df['Median Income Per Person'].notna()]


features = df.drop('Median Income Per Person', axis=1).values
target = df['Median Income Per Person'].values

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)


print('MSE score: {}'.format(metrics.mean_squared_error(y_test, y_pred)))