import numpy as np
import pandas as pd

df = pd.read_csv('sample_cars.csv') #loading the dataset

df_zip = pd.read_csv('zip_codes.csv') #importing zip code data


#We noticed in the sampling report that the followign attributes had the following issues:
#Scofflaw Indicator is highly imbalanced (97.7%)	Imbalance
#Suspension Indicator is highly imbalanced (91.2%)	Imbalance
#Revocation Indicator is highly imbalanced (99.2%)	Imbalance
#Maximum Gross Weight has 471603 (83.1%) missing values	Missing
#Passengers has 556875 (98.1%) missing values


#We will keep the suspension indicator, but we will drop the remaining variables from the dataset. 
#We will keep the suspension indicators because I think it's intresting. 

df.drop(columns=['Scofflaw Indicator', 'Revocation Indicator', 'Maximum Gross Weight', 'Passengers'], inplace= True)

df['Zip'].replace('06390', '6390', inplace=True)
df_zip['placeName'].replace('06390', '6390', inplace=True)


df_zip.set_index('placeName', inplace= True)
# Define the function to include median income
def med_income(zip):
    return(df_zip.loc[zip, 'Value:Median_Income_Person'])

# adding the column to our df
df['Median Income Per Person'] = df['Zip'].apply(med_income)


df.to_csv('sample_cars.csv', index= False) #exporting smaller dataset




