#%%
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime

#%% NOTE: datetime
ebola = pd.read_csv(r'data/country_timeseries.csv')
# or
# ebola = pd.read_csv(r'data/country_timeseries.csv', parse_dates=[0]) # pointing at the 
# column with dates
print(ebola.iloc[:5, :5])

ebola['date_dt'] = pd.to_datetime(ebola['Date'])
# or
# ebola['date_dt'] = pd.to_datetime(ebola['Date'], format='%m/%d/%Y')

# %%
banks = pd.read_csv(r'data/banklist.csv')
# automatic timedate parsing
# banks = pd.read_csv(r'data/banklist.csv', parse_dates=[5, 6])

# %%
ebola = pd.read_csv(r'data/country_timeseries.csv', index_col='Date', parse_dates=['Date'])
print(ebola.head())

date_range = pd.date_range(ebola.index.min(), ebola.index.max()) # creates all dates within the range
# if any date is missing

# %%
down = ebola.resample('M').mean()
print(down)
# %%
