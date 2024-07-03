import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('sample_cars.csv') #loading the sampled data set 
profile = ProfileReport(df, title="Profiling Report", correlations ={"pearson": {"calculate": True}},)
profile.to_file("cars_sample_report.html") #exporting the report