import numpy as np
import pandas as pd

df = pd.read_csv('Kapstone/cars_dataset.csv') #loading the dataset, this dataset is too big to include on github

df_zip = pd.read_csv('zip_codes.csv') #importing zip code data

df = df[df['Zip'].isin(df_zip['placeName'])]

counts = {}
for value in df['Make']:
    counts[value] = counts.get(value, 0) + 1 #counts totoal number of cars of a certain make in NY

makes_counts = {k:v for (k,v) in counts.items() if v > 30000} #setting threshhold to 30,000 cars in registration data

makes = list(makes_counts.keys())

df = df[df['Make'].isin(makes)]

area_codes = df['Zip'].unique()

#This is going to be scuffed and long but it'll run once so its fine:
df_new = pd.DataFrame(index=area_codes, columns= makes)

for area in area_codes:
    df_temp = df.loc[(df['Zip'] == area)].copy()
    temp = {}
    for value in df_temp['Make']:
        temp[value] = temp.get(value, 0) + 1
    for car in temp:
        df_new.loc[area, car] = temp[car]


df_new = df_new.replace(np.nan, 0) #in case we have any stragellers


df_new = df_new.reset_index() 
df_new = df_new.rename(columns={"index": "Zip"}) #If i wanted to work with pointers I would be coding in C++...

df_zip.set_index('placeName', inplace= True)
# Define the function to include median income
def med_income(zip):
    return(df_zip.loc[zip, 'Value:Median_Income_Household'])

# adding the column to our df
df_new['Median Income Per Person'] = df_new['Zip'].apply(med_income)


df_new.to_csv('sample_zips.csv', index= False) #exporting smaller dataset