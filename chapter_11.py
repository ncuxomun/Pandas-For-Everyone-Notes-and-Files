#%%
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

#%% NOTE: GENERALZIED LINEAR MODELS
# Simple linear regression
acs = pd.read_csv(r'data/acs_ny.csv')
print(acs.head())

# %%
# creating binary variable
acs['get150k'] = pd.cut(acs['FamilyIncome'], [0, 150000, acs['FamilyIncome'].max()], labels=[0, 1])
acs['get150k_i'] = acs['get150k'].astype(int)

# %% #using statsmodel
model = smf.logit('get150k_i ~ HouseCosts + NumWorkers + OwnRent + NumBedrooms + FamilyType', data=acs)

results = model.fit()

print(results.summary())

# %%
odds_ratio = np.exp(results.params)
print(odds_ratio)

# %%
# Poisson regression
model = smf.poisson('NumChildren ~ FamilyType + OwnRent + get150k_i', data=acs)
results = model.fit()

print(results.summary())

odds_ratio = np.exp(results.params)
print(odds_ratio)
