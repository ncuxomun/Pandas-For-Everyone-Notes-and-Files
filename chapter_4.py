#%%
from ntpath import join
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# DATA MANIPULATION
# concatination
df1 = pd.read_csv(r'data/concat_1.csv')
df2 = pd.read_csv(r'data/concat_2.csv')
df3 = pd.read_csv(r'data/concat_3.csv')

row_concat = pd.concat([df1, df2, df3]) # vertical stacking
print(row_concat)
# %%
new_row_df = pd.DataFrame([['n1', 'n2', 'n3', 'n3']],
                          columns=['A', 'B', 'C', 'D'])

print(pd.concat([df1, new_row_df])) # by row

#pd.concat([df1, new_row_df]) == df1.append(new_row_df)
print(df1.append(new_row_df)) # append is deprecated

# whatever is being concatenated must have the same column names
# %%
# ignore index, and start incrementing onto preceding one
print(pd.concat([df1, new_row_df], ignore_index=True))

# %%
# concat by columns
col_concat = pd.concat([df1, df2, df3], axis=1)  # horiz stacking ->
print(col_concat)

# adding a new column
col_concat['new_column'] = ['n1', 'n2', 'n3', 'n3']
print(col_concat)
# %%
# what if the columns/row indices don't match
df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'A', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

row_concat = pd.concat([df1, df2, df3])  # vertical stacking
print(row_concat)

# joining by common columns
row_concat = pd.concat([df1, df2, df3], join='inner') 
print(row_concat)

# %%
# concat by different row indices
df1.index = [0, 1, 2, 3]
df2.index = [2, 5, 6, 7]
df3.index = [0, 2, 5, 7]

col_concat = pd.concat([df1, df2, df3], axis=1)  # horiz stacking ->
print(col_concat)

col_concat = pd.concat([df1, df2, df3], axis=1, join='inner')  # horiz stacking ->
print(col_concat)

# %%
# Merging multiple datasets
person = pd.read_csv(r'data/survey_person.csv')
site = pd.read_csv(r'data/survey_site.csv')
survey = pd.read_csv(r'data/survey_survey.csv')
visited = pd.read_csv(r'data/survey_visited.csv')

# %%
#NOTE one-to-one merging
visited_sub = visited.loc[[0, 2, 6], ]
o2o = site.merge(visited_sub, left_on='name', right_on='site')
print(o2o)

# NOTE: merging columns don't have same names, thus left_ & right_on instead of left/right
# merging happens by matching values in the requested columns

# %%
# NOTE: many-to-one merging
m2o = site.merge(visited, left_on='name', right_on='site')
print(m2o)
# %%
# NOTE:  many-to-many
ps = person.merge(survey, left_on='ident', right_on='person')
vs = visited.merge(survey, left_on='ident', right_on='taken')

# by list of matching columns values
ps_vs = ps.merge(vs, left_on=['ident', 'taken', 'quant', 'reading'],
                 right_on=['person', 'ident', 'quant', 'reading'])

print(ps_vs.head())
# %%
# NOTE: working with MISSING values (NaNs)
import numpy as np

print(pd.isnull(np.NAN)) #checking for nulls
print(pd.isna(np.NAN))
# %%
# Working with missing values
ebola = pd.read_csv(r'data/country_timeseries.csv')
ebola.head()

# %%
# count no. non-missing values
# print(ebola.count())
num_missing = ebola.shape[0] - ebola.count()

print(f'Missing values: {num_missing}')

# count total num of non-zeros
print(np.count_nonzero(ebola.isnull()))
# %%
# NOTE: Recoding/Replacing NAN values with somthg
print(ebola.fillna(0))
# %%
# Fill Forward/Backward
# NOTE: Forward uses last non-zero value for the next missing value
# Backward uses newest last value to replace missing one
print(ebola.fillna(method='ffill'))
print(ebola.fillna(method='bfill'))

# %%
# NOTE: Or by INTERPOLATING
print(ebola.interpolate())
# df.dropna drops all NANs and keeps complete sets only
# creating new columns with missing values would lead to columns with missing values too

# values can still me calculated if stated explicitly
# such as ebola.column_with_nan.sum(skipna=True) --> skips NAN and sums values only
# %%
#NOTE: Tidy data, pivot and stuff
pew = pd.read_csv(r'data/pew.csv')
pew.head()
# %%
long_pew = pd.melt(pew, id_vars='religion')
long_pew.head()
# %%
billboard = pd.read_csv(r'data/billboard.csv')
billboard_long = pd.melt(billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                         var_name='week', value_name='rating')
# %%
# columns with multiple variables
ebola = pd.read_csv(r'data/country_timeseries.csv')

# %%
# split and combine in a single step
ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
var_split = ebola_long.variable.str.split('_', expand=True)
var_split.columns = ['status', 'country']
ebola_parsed = pd.concat([ebola_long, var_split], axis=1)
print(ebola_parsed)

# %%
#NOTE cool one-liner
ebola_long['status'], ebola_long['country'] = zip(*ebola_long.variable.str.split('_'))

print(ebola_long)

# %%
billboard_songs = billboard_long[['year', 'artist', 'track', 'time']]
billboard_songs = billboard_songs.drop_duplicates()
billboard_songs['id'] = range(len(billboard_songs))

print(billboard_songs)
# %%
# merging based columns and assigning respective IDs
billboard_ratings = billboard_long.merge(billboard_songs, on=['year', 'artist', 'track', 'time'])
print(billboard_ratings)
# %%
