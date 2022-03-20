#%%
import pandas as pd

#%%
# loading gapminder dataset
df = pd.read_csv('../data/gapminder.tsv',  sep='\t')
# %%
df.head()

print(type(df))

print(df.shape)
# %% colummns
print(df.columns)

# what datatypes each column is
print(df.dtypes)

# get info on data, including data types for each column
print(df.info())

# %%
# ** 1.3 looking at columns, rows, and cells **

# get the column and set new variable
country_df = df['country']
print(country_df.head())

# making a subset
subset = df[['country', 'year']]
print(subset.tail())

# %%
# subsetting columns
# .loc - subset based on index label (row name)
# .iloc - subset based on row index (row number)

# print n-th row
print(df.loc[88])

# last row as '-1' prompts error
last_row_index = df.shape[0] - 1
print(df.loc[last_row_index]) # same as df.tail([n=1])

# %%
# subsetting multiple rows
print(df.loc[[2, 55, 564]])

# mixing columns and rows
# df.iloc[[rows], [columns]]
# df.loc[[rows], [columns]]

# subsetting columns
subset = df.loc[:, ['year', 'pop']] # or df.iloc[:, [2, 4]] --> iloc allows column indeces
print(subset.head())

# %%
# subsetting by range
small_range = list(range(5)) # range(3, 8) # range(0, 6, 2) # evert other integer

# subset with range
subset = df.iloc[:, small_range]

# OR by python CLICING
subset = df.iloc[:, 3:6]
subset = df.iloc[:, 0:6:2]  # same df.iloc[:, 0::2] ::2

print(subset.head())

# %%
# subsetting rows and columns
print(df.loc[42, 'country']) # same as df.iloc[42, 0]

print(df.iloc[[0, 3, 55], [2, 5]])

print('\n')
# better if we use columns by their names
print(df.loc[[0, 3, 55], ['year', 'gdpPercap']])

# %%
# 1.4 Grouped and Aggregated Calculations

# Grouped means

# mean of lifeExp given a year
grouped_by_year = df.groupby('year')['lifeExp'].mean()
print(grouped_by_year)

# means for several variables and columns
grouped_by_year_continent = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(grouped_by_year_continent)

# resets/flattens dataset
print(grouped_by_year_continent.reset_index())

# %%
# Grouped frequency counts, unique counts
print(df.groupby('continent')['country'].nunique())

# Grouped frequency counts, columns repetions given groupby condition
print(df.groupby('continent')['country'].value_counts())

# %%
# 1.5 basic plot
grouped_by_year_lifeExp = df.groupby('year')['lifeExp'].mean()
grouped_by_year_lifeExp.plot()

# %%
