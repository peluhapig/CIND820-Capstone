import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('cars_dataset.csv')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("cars_summary_report.html")
