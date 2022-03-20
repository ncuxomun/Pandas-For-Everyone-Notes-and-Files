#%% Plotting
from cProfile import label
from posixpath import split
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
tips = sns.load_dataset("tips")
# %%
def color(sex=None):
    if sex == 'Female':
        return 0
    else:
        return 1
    
tips['color_sex'] = tips['sex'].apply(color)

# apply(function)
# %%
plt.figure(figsize=(5, 5))
plt.scatter(tips['total_bill'], tips['tip'], s=tips['tip']*20, c=tips['color_sex'])
plt.xlabel('total bill'); plt.ylabel('tip')
plt.tight_layout()
plt.show()
# %%
# bar plot bsed on frequencies
plt.figure(figsize=(5, 5))
sns.countplot('day', data=tips)
plt.xlabel('day of a week')
plt.ylabel('freq')
plt.tight_layout()
plt.show()

# %%
# "scatter" plot including fitting line on/off
plt.figure(figsize=(5, 5))
sns.regplot(x='total_bill', y='tip', data=tips, fit_reg=True)
plt.xlabel('total bill')
plt.ylabel('tip')
plt.tight_layout()
plt.show()

# %%
# "scatter" plot including fitting line on/off, similar but w/o boxes
plt.figure(figsize=(5, 5))
sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=True, hue='sex')
plt.tight_layout()
plt.show()

# %%
# "scatter" plot including joint distributions
plt.figure(figsize=(7, 7))
joint = sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
joint.set_axis_labels(xlabel='total bill', ylabel='tip')
joint.fig.suptitle('data_test')
plt.tight_layout()
plt.show()

# %%
# density plot including joint distributions
plt.figure(figsize=(5, 5))
dens = sns.kdeplot(x=tips['total_bill'], y=tips['tip'], shade=True)
plt.tight_layout()
plt.show()

# %%
# bar plot
plt.figure(figsize=(5, 5))
bars = sns.barplot(x='time', y='tip', data=tips, hue='sex')
plt.tight_layout()
plt.show()

# %%
# box plot 
plt.figure(figsize=(5, 5))
bars = sns.boxplot(x='time', y='tip', data=tips)
plt.tight_layout()
plt.show()

# %%
# violin plot = box_plot but with density distributions
plt.figure(figsize=(5, 5))
bars = sns.violinplot(x='time', y='tip', data=tips, hue='sex', split=True)
plt.tight_layout()
plt.show()

# %%
# pairwise - between each variable in the set
plt.figure(figsize=(10, 10))
sns.pairplot(data=tips, hue='sex')
plt.tight_layout()
plt.show()

# %%
# "scatter" plot including fitting line on/off, similar but w/o boxes
plt.figure(figsize=(5, 5))
sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=False, hue='sex',
           markers=['^', 'o'], scatter_kws={'s': tips['size']*20})
plt.tight_layout()
plt.show()

# %%
# facet
facet = sns.FacetGrid(data=tips, row='smoker', col='time',hue='sex')
facet.map(plt.scatter, 'total_bill', 'tip')
# %%
