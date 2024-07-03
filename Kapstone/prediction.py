from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics
import pandas as pd


df = pd.read_csv('sample_cars.csv') #loading the dataset

df = df.drop(['VIN','City','State','Zip','County','Color','Body Type', 'Registration Class','Reg Valid Date','Reg Expiration Date','Unladen Weight'], axis=1) #dropping columns which will be correlated with our zip code or irrelevant for prediction 
df.dropna(inplace=True)

#One-hot encoding catagorical variables
cat_cols=['Record Type','Make','Fuel Type','Suspension Indicator']
df = pd.get_dummies(df, columns=cat_cols, prefix = cat_cols)

features = df.drop('Median Income Per Person', axis=1).values
target = df['Median Income Per Person'].values

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)


# regression coefficients
print('Coefficients: ', reg.coef_)

# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, y_test)))