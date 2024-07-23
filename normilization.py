import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data_classes.csv')

df2 = df.drop(['Classified Income','Zip'], axis = 1)

#lets get the lengths:
rows = (df2.shape[0] )
col = (df2.shape[1] )

print(rows,col)
i= 0

while i <rows :
    j=0
    tot = 0
    while j < col:
       print(str(i) +", " + str(j))
       tot += df2.iloc[i,j] #adding alll the rows
       j += 1
    j=0
    while j < col:
        df2.iloc[i,j] = df2.iloc[i,j]/tot #diving by the total and setting the value
        j += 1
    i += 1

df2['Zip'] = df['Zip']
df2['Classified Income'] = df['Classified Income']

df2.to_csv('norm_data_classes.csv') #exporting