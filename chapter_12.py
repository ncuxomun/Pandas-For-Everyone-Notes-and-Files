#%%
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt

#%% NOTE: MODEL DIAGNOSTICS
# Simple linear regression
housing = pd.read_csv(r'data/housing_renamed.csv')
print(housing.head())
# %%
house1 = smf.glm('value_per_sq_ft ~ units + sq_ft + boro', data=housing).fit()

print(house1.summary())

# %%
fig, ax = plt.subplots()
ax = sns.regplot(x=house1.fittedvalues, y=house1.resid_deviance, fit_reg=False)
plt.tight_layout()
plt.show()
# %%
res_df = pd.DataFrame({'fitted': house1.fittedvalues,
                       'resid': house1.resid_deviance,
                       'boro': housing['boro']})

fig = sns.lmplot(x='fitted', y='resid', data=res_df, hue='boro', fit_reg=False)
plt.tight_layout()
plt.show()

# %% NOTE: Q-Q plot to check if data follow normal distribution
import statsmodels

resid = house1.resid_deviance.copy()
fig = statsmodels.graphics.gofplots.qqplot(resid, line='r')
plt.tight_layout()
plt.show()

# %%
# MULTIPLE MODELS
f1 = 'value_per_sq_ft ~ units + sq_ft + boro'
f2 = 'value_per_sq_ft ~ units * sq_ft + boro'
f3 = 'value_per_sq_ft ~ units + sq_ft * boro + type'
f4 = 'value_per_sq_ft ~ units + sq_ft + boro + sq_ft * type'
f5 = 'value_per_sq_ft ~ boro + type'

house1 = smf.ols(f1, data=housing).fit()
house2 = smf.ols(f2, data=housing).fit()
house3 = smf.ols(f3, data=housing).fit()
house4 = smf.ols(f4, data=housing).fit()
house5 = smf.ols(f5, data=housing).fit()

# %%
model_results = pd.concat([house1.params, house2.params, house3.params, house4.params, house5.params],
                          axis=1).rename(columns=lambda x: 'house' + str(x + 1)).reset_index().rename(columns={'index': 'param'}).melt(id_vars='param', var_name='model', value_name='estimate')

print(model_results.head())
# %% ANOVA
model_names = ['house1', 'house2', 'house3', 'house4', 'house5']
house_anova = statsmodels.stats.anova.anova_lm(house1, house2, house3, house4, house5)
house_anova.index = model_names

print(house_anova)

# %%
# AIC and BIC
house_models = [house1, house2, house3, house4, house5]

house_aic = list(map(statsmodels.regression.linear_model.RegressionResults.aic, house_models))
house_bic = list(map(statsmodels.regression.linear_model.RegressionResults.bic, house_models))

abic = pd.DataFrame({'model': model_names, 'aic': house_aic, 'bic': house_bic})
print(abic)

# %% NOTE: K-Fold Cross-Validation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(
    pd.get_dummies(housing[['units', 'sq_ft', 'boro']], drop_first=True),
    housing['value_per_sq_ft'], test_size=0.20, random_state=42)

lr = LinearRegression().fit(X_train, y_train)
print(lr.score(X_test, y_test))

# %%
