#%%
import numpy as np
import pandas as pd
import seaborn as sns

#%% NOTE: Groupby: Split-Apply-Combine
df = pd.read_csv(r'data/gapminder.tsv', sep='\t')

avg_life_exp_by_year = df.groupby('year').lifeExp.mean() # == df.groupby('year').['lifeExp'].mean()
print(avg_life_exp_by_year)

avg_life_exp_by_year = df.groupby('year').lifeExp.aggregate(np.mean) # == df.groupby('year').['lifeExp'].mean()
print(avg_life_exp_by_year)
#NOTE: aggregate can take any function, e.g. func(val), where val is a series of values
# in case func(val, x), we need to pass column.aggregate(func, x=**), x is the string name

print('\nUnique years: ', df['year'].unique())

print('\nSubset for year 1952 only:')
print(df.loc[df['year'] == 1952, :])

# %%
cont_desribe = df.groupby('continent')['lifeExp'].describe()
print(cont_desribe)
# %%
# NOTE: multiple functions in aggregate
gdf = df.groupby('year')['lifeExp'].aggregate([np.count_nonzero, np.mean, np.std])
print(gdf)
# %%
# Data transform
from scipy.stats import zscore

sp_z_grouped = df.groupby('year')['lifeExp'].transform(zscore)
# %% NOTE: FILTERING
tips = sns.load_dataset('tips')

print(tips['size'].value_counts())

tips_filtered = tips.groupby('size').filter(lambda x: x['size'].count() >= 30)
print(tips_filtered)
# count() counts no. of observations in each group

# %% Multiple groups
by_sex_time_mean = tips.groupby(['sex', 'time']).mean()
print(by_sex_time_mean)
print('\nWith indices reset \n')
print(by_sex_time_mean.reset_index())
# %%
