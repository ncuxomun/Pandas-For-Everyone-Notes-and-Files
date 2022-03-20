#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# DATA Types
tips = sns.load_dataset('tips')
print(tips.dtypes)

#%% Data Conversion
# creating a string column from category
tips["sex_str"] = tips['sex'].astype(str)
print(tips.dtypes)

# %%
# creating category instead of string
tips["sex_cat"] = tips['sex'].astype('category')
print(tips.dtypes)

# %%
