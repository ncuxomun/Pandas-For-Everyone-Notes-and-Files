#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
# NOTE: APPLY --> takes a functions and applies for each row/column of df simul

def my_sq(x):
    return x ** 2

df = pd.DataFrame({'a': [10, 20, 30],
                   'b': [20, 30, 40]
                   })
print(df['a'].apply(my_sq))

def my_sq(x, exp):
    return x ** exp

print(df['a'].apply(my_sq, exp=3))
# %%
# operations on DF and row/column
print(df.apply(my_sq, exp=3, axis=1))

print(df.apply(my_sq, exp=3, axis=0))
# %%
tit = sns.load_dataset("titanic")
print(tit.info())
# %%
# counting, for each variable
def count_missing(vec):
    nul_vec = pd.isnull(vec)
    null_count = np.sum(nul_vec)
    return null_count

def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return num / dem

def prop_complete(vec):
    return 1 - prop_missing(vec)

print("Missing \n", tit.apply(count_missing))
print("Data proportion complete \n", tit.apply(prop_complete))
# %%
# NOTE: Vectorizing using numpy.vectorize

df = pd.DataFrame({'a': [10, 20, 30],
                   'b': [20, 30, 40]})

@np.vectorize
def v_avg_2_mod(x, y):
    """ compute average """
    return (x + y) / 2

print(v_avg_2_mod(df['a'], df['b']))

# %%
# NOTE: Vectorizing using numba.vectorize
import numba

@numba.vectorize
def v_avg_2_num(x, y):
    """ compute average """
    return (x + y) / 2

print(v_avg_2_num(df['a'].values, df['b'].values)) #.values because numba doesn't understand Pandas

# %% NOTE: Lambdas
import re
docs = pd.read_csv(r'data/doctors.csv', header=None)

pa = re.compile('\w+\s+\w+')

docs_lambda = docs[0].apply(lambda x: pa.match(x).group())
print(docs_lambda)
# %%
