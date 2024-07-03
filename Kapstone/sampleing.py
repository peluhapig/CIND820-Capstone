import numpy as np
import pandas as pd

df = pd.read_csv('Kapstone/cars_dataset.csv') #loading the dataset, this dataset is too big to include on github

df_zip = pd.read_csv('zip_codes.csv') #importing zip code data

# As our data set is 12.2 million, it is impracticle to run our projet on the full dataset before we train out model. 
# Therefore we will use stratified sampling to ensure our Zip Code percentages stay the same

#We notice that There are 11,337 distinct Zip codes , when there in reality are only 1727 Zip Codes as we see from out zip code data,
# As our datset is so large we will simply remove all of the entries which are not in the acceptable zip-code range

df = df[df['Zip'].isin(df_zip['placeName'])]

#Then we will sample

df = df.groupby('Zip').sample(frac=0.4, random_state= 42) # This will group by Zip Code, and then sample 40% of them from each one. (around 2000 vehicles per zip code)
df.to_csv('sample_cars.csv', index= False) #exporting smaller dataset