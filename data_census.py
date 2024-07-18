import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('sample_zips.csv')
#

df_temp = pd.read_csv('mi.csv')

mi_df = df_temp[['NAME','S1903_C03_001E']]

temp = mi_df['NAME'].str.split(pat= ' ', expand= True)

mi_df['Zip'] = temp[1]

mi_df.drop('NAME',axis=1 ,inplace= True)
mi_df.drop(0, inplace= True)
mi_df['S1903_C03_001E'] = mi_df['S1903_C03_001E'].str.replace(',','')
mi_df['S1903_C03_001E'] = mi_df['S1903_C03_001E'].str.replace(' ','')
mi_df['S1903_C03_001E'] = mi_df['S1903_C03_001E'].str.replace('0+','1')
mi_df['S1903_C03_001E'] = mi_df['S1903_C03_001E'].str.replace('-','')
mi_df['S1903_C03_001E'] = pd.to_numeric(mi_df['S1903_C03_001E'])
mi_df['Zip'] = pd.to_numeric(mi_df['Zip'])

d_threshold_1 = 61667
d_threshold_2 = 76046
d_threshold_3 = 101250
d_threshold_4 = 160273

classified_income = []
for k in mi_df['S1903_C03_001E']:
    if k <= d_threshold_1:
        classified_income.append(0)
    elif k < d_threshold_2:
        classified_income.append(1)
    elif k < d_threshold_3:
        classified_income.append(2)
    elif k < d_threshold_4:
        classified_income.append(3)
    elif k == None:
        classified_income.append(None)
    else:
        classified_income.append(4)
mi_df['Class'] = classified_income


# Define the function to include median income
def med_income(zip):
    return(mi_df.loc[int(zip), 'Class'])


mi_df.reset_index(inplace= True)
mi_df.set_index('Zip', inplace = True)
#11425 = 11209
#13794 = 13803
#13064 = 13156
#13677 = 13617
#13362 = 13425
#13845 = 13734
#11351 = 11357
#12089 = 12090
#13341 = 13323
mi_df['Zip'] = mi_df.index
dic = {'Zip': [11425,13794,13064,13677,13362,13845,11351,12089,13341],
         'S1903_C03_001E': [mi_df.loc[11209 ,'S1903_C03_001E'],mi_df.loc[13803 ,'S1903_C03_001E'],mi_df.loc[13156 ,'S1903_C03_001E'],mi_df.loc[13617 ,'S1903_C03_001E'],mi_df.loc[13425 ,'S1903_C03_001E'],mi_df.loc[13734 ,'S1903_C03_001E'],mi_df.loc[11357 ,'S1903_C03_001E'],mi_df.loc[12090 ,'S1903_C03_001E'],mi_df.loc[13323 ,'S1903_C03_001E']], 
       'Class': [mi_df.loc[11209 ,'Class'],mi_df.loc[13803 ,'Class'],mi_df.loc[13156 ,'Class'],mi_df.loc[13617 ,'Class'],mi_df.loc[13425 ,'Class'],mi_df.loc[13734 ,'Class'],mi_df.loc[11357 ,'Class'],mi_df.loc[12090 ,'Class'],mi_df.loc[13323 ,'Class']]}
df2 = pd.DataFrame(dic)
mi_df = mi_df._append(df2, ignore_index = True)
mi_df.set_index('Zip',inplace = True)
mi_df['Zip'] = mi_df.index
# adding the column to our df
df['Classified Income'] = df['Zip'].apply(med_income)
df.drop('Median Income Per Person', axis= 1, inplace= True)
df.to_csv('data_classes.csv')