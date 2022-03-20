#%%
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt

#%% NOTE: Clustering
# Regularization
wine = pd.read_csv(r'data/wine.csv')
print(wine.head())

# dropping column that correlates closely
wine = wine.drop('Cultivar', axis=1)
print(wine.head())
# %%
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42).fit(wine.values)
print(kmeans)

# %%
print(np.unique(kmeans.labels_, return_counts=True))

k_means = pd.DataFrame(kmeans.labels_, columns=['cluster'])
# %%
# NOTE Dimensionality reduction w/ PCA
from sklearn.decomposition import PCA

pca = PCA(n_components=2).fit(wine)
pcs_transform = pca.transform(wine)

pcs_transform_df = pd.DataFrame(pcs_transform, columns=['pc1', 'pc2'])

# concat w/ labels
k_means = pd.concat([k_means, pcs_transform_df], axis=1)
print(k_means.head())

fig = sns.lmplot(x='pc1', y='pc2', data=k_means, hue='cluster', fit_reg=False)
plt.show()

# %%
# NOTE: Hierarchical clustering
from scipy.cluster import hierarchy
wine = pd.read_csv(r'data/wine.csv')

# dropping column that correlates closely
wine = wine.drop('Cultivar', axis=1)

wine_complete = hierarchy.complete(wine)

fig = plt.figure()
dn = hierarchy.dendrogram(wine_complete)
plt.show()

# %%
