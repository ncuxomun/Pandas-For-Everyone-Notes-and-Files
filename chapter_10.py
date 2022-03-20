#%%
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

#%% NOTE: LINEAR MODELS: statsmodels and sklearn regression
# Simple linear regression
tips = sns.load_dataset("tips")

model = smf.ols(formula='tip ~ total_bill', data=tips)

# model fitting
results = model.fit()
print(results.summary())

# %%
# using sklearn
from sklearn import linear_model as lm

lr_model = lm.LinearRegression()

tips_hat = lr_model.fit(X=tips["total_bill"].values.reshape(-1, 1),
                        y=tips["tip"].values.reshape(-1, 1))

# not so statistic-like results

# %%
# NOTE: Multi-variate Regression
model = smf.ols(formula='tip ~ total_bill + size', data=tips)

# model fitting
results = model.fit()
print(results.summary())

# %%
# stats deals with categorical vars automatically
model = smf.ols(formula='tip ~ total_bill + size + sex + day + time', data=tips)

# model fitting
results = model.fit()
print(results.summary())

# %%
# sklearn needs categorical vars converted first
tips_dummy = pd.get_dummies(tips[['total_bill', 'size', 'sex', 'day', 'time']])
# to drop reference variables
tips_dummy_ref_dropped = pd.get_dummies(tips[['total_bill', 'size', 'sex', 'day', 'time']], drop_first=True)

lr_model = lm.LinearRegression()

tips_hat = lr_model.fit(X=tips_dummy_ref_dropped,
                        y=tips["tip"])

# %%
