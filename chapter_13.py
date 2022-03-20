#%%
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#%% NOTE: MODEL DIAGNOSTICS
# Regularization
acs = pd.read_csv(r'data/acs_ny.csv')
print(acs.head())

response, predictors = dmatrices('FamilyIncome ~ NumBedrooms + NumChildren + NumPeople +' \
                                'NumRooms + NumUnits + NumVehicles + NumWorkers + OwnRent +' \
                                'YearBuilt + ElectricBill + FoodStamp + HeatingFuel + Insurance + Language',
                                data = acs)


# %%
X_train, X_test, y_train, y_test = train_test_split(predictors, response, random_state = 0)

lr = LinearRegression(normalize=True).fit(X_train, y_train)

model_coefs = pd.DataFrame(list(zip(predictors.design_info.column_names, lr.coef_[0])),
                           columns=['variable', 'coef_lr'])

print(model_coefs)

# %%
print('Train R2 score: ', lr.score(X_train, y_train))
print('Test R2 score: ', lr.score(X_test, y_test))

# this model not overfitting
# LASSO --> some coeffs are 0 Ridge --> coefs are not close to 0 only
# %%

# NOTE: LASSO Regression (Regression with L1 reg)
from sklearn.linear_model import Lasso

lasso = Lasso(normalize=True, random_state=0).fit(X_train, y_train)

lasso_coefs = pd.DataFrame(list(zip(predictors.design_info.column_names, lasso.coef_)),
                           columns=['variable', 'coef_lasso'])

model_coefs = pd.merge(model_coefs, lasso_coefs, on='variable')
print(model_coefs)

print('Train R2 score: ', lasso.score(X_train, y_train))
print('Test R2 score: ', lasso.score(X_test, y_test))

# %%
# NOTE: RIdge regression
from sklearn.linear_model import Ridge

ridge = Ridge(normalize=True, random_state=0).fit(X_train, y_train)

ridge_coefs = pd.DataFrame(list(zip(predictors.design_info.column_names, ridge.coef_)),
                           columns=['variable', 'coef_ridge'])

model_coefs = pd.merge(model_coefs, ridge_coefs, on='variable')
print(model_coefs)

print('Train R2 score: ', ridge.score(X_train, y_train))
print('Test R2 score: ', ridge.score(X_test, y_test))

# %%
# NOTE: ElasticNet - combines both Ridge and LASSO
from sklearn.linear_model import ElasticNet

en = ElasticNet(random_state=0).fit(X_train, y_train)

en_coefs = pd.DataFrame(list(zip(predictors.design_info.column_names, en.coef_)),
                           columns=['variable', 'coef_en'])

model_coefs = pd.merge(model_coefs, en_coefs, on='variable')
print(model_coefs)

print('Train R2 score: ', en.score(X_train, y_train))
print('Test R2 score: ', en.score(X_test, y_test))

# %%
# NOTE: ElasticNet w/ Cross-Validation
from sklearn.linear_model import ElasticNetCV

en_cv = ElasticNetCV(cv=5, random_state=0).fit(X_train, y_train)

en_cv_coefs = pd.DataFrame(list(zip(predictors.design_info.column_names, en_cv.coef_)),
                           columns=['variable', 'coef_en'])

model_coefs = pd.merge(model_coefs, en_cv_coefs, on='variable')
print(model_coefs)

print('Train R2 score: ', en_cv.score(X_train, y_train))
print('Test R2 score: ', en_cv.score(X_test, y_test))

# %%
