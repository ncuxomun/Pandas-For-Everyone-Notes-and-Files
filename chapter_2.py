#%%
import pandas as pd

#%%
# creating and working with series
s = pd.Series(['banana', 42])
print(s)

# manually assigning index values to a series
s = pd.Series(['McKinney', 'Creater of Pandas'], index=['Person', 'Who'])
print(s)

# Person and Who for 0 and 1, respectively

# %%
# creating a DataFrame
scientists = pd.DataFrame(
    {
        'Name': ['R. Franklin', 'W. Gosset'],
        'Occupation': ['Chemist', 'Statistician'],
        'Born': ['1920-07-25', '1876-06-13'],
        'Died': ['1957-07-25', '1937-06-13']
    }
)

print(scientists)

# set by order index
scientists = pd.DataFrame(data=
                          {
                          'Occupation': ['Chemist', 'Statistician'],
                          'Born': ['1920-07-25', '1876-06-13'],
                          'Died': ['1957-07-25', '1937-06-13']
                          },
                          index=['R. Franklin', 'W. Gosset'],
                          columns=['Occupation', 'Born', 'Died']
)

print(scientists)
# %%
# ordered dictionary
from collections import OrderedDict # remebers insertion order, pd.DataFrame does not

scientists = pd.DataFrame(OrderedDict([
    ('Name', ['R. Franklin', 'W. Gosset']),
    ('Occupation', ['Chemist', 'Statistician']),
    ('Born', ['1920-07-25', '1876-06-13']),
    ('Died', ['1957-07-25', '1937-06-13']) 
                                     ])
)

print(scientists)

# %%
# 2.3 The Series
# set by order index
scientists = pd.DataFrame(data={
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1957-07-25', '1937-06-13']
},
    index=['R. Franklin', 'W. Gosset'],
    columns=['Occupation', 'Born', 'Died']
)

print(scientists.loc['W. Gosset'].keys())
# the two are same
print(scientists.loc['W. Gosset'].index)

# %%
# the Series Methods
occ = scientists['Occupation']

print(occ)
# %%
scientists = pd.read_csv(r'data/scientists.csv',  sep=',')

# adding additional columns
# format 'Born' dates as datetime
born_dates = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_dates = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
# print(born_dates)

# combining the two new columns
scientists['born_dt'], scientists['died_dt'] = (born_dates, died_dates)
print(scientists)

# %%
# 2.6 Exporting and Importing Data

# saving to PICKLE
# df.to_pickle('.../x_df.pickle') - saves pickle file (binary format)

# importing from pickle
# df_from_pickle = df.read_pickle('/x.pickle')

#### pickle extensions are: .p, .pkl, and .pickle

# saving to CSV (comma-separated values)
# df.to_csv('.../x_df.csv') - saves CSV file

# if tab-separated, then df.to_csv('.../x_df.tsv', sep='\t') - saves TSV file

# importing from csv
# df_from_csv = df.read_csv('/x.csv')

# TODO: to_csv/tsv will save INDEX values (e.g., 0, 1,..) to avoid that do
# df.to_csv('.../x_df.csv', index=False) - saves CSV file w/o indices

#%%
# Saving to and Reading from EXCEL
# TODO: convert Series to DataFrame first if none 

# series_df = names.to_frame()
# import openpyxl
# names_df.to_excel('.../AA.xlsx')

# or specifically
# import openpyxl
# names_df.to_excel('.../AA.xlsx', sheet_name='XXXXX', index=False) # w/ specific sheet name

# save to SQL and STATA
# df.to_sql('') & df.to_stata('')