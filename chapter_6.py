#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
# Strings and Text data
word = "grail"

# %% slicing increment [::x] - every x-th element, starting w/ 0
print(word[::2])
# %% # join
d1 = '40'
m1 = "46'"
s1 = '54.2"'
coords = ' '.join([d1, m1, s1])
print(coords)


# %% formatting
x_ = 7 / 97834
print("gone with the wind in {0:.2} or {0:.2%} seconds".format(x_))
# NOTE: 0 is the first index, .2 is how many decimal points to print

# padding
print("My ID is {0:07d}".format(69)) # padding wth 0 from left and make it 7 character long in total

# %%
#NOTE REgEx
import re
tele_num = '1234356'

m = re.match(pattern='\d\d\d\d\d\d\d', string=tele_num) # patter=\d{7}
print(bool(m))


tele_num_spaces = '123 4 356'
p = '\d{3}\s?\d\s?\d{3}'

m = re.match(pattern=p, string=tele_num_spaces)  # patter=\d{7}
print(bool(m))

print(m.group()) # return string matched
# %% # find a patter
p = "\d"
s = "13 johnnie walkerm war hgearo, 2333 peter capaldi"
m = re.findall(pattern=p, string=s)
print(m)
# %%
# compiling into patter
p = re.compile('\d+')
s = "13 johnnie walkerm war hgearo, 2333 peter capaldi"
m = p.findall(s)
print(m)

# %%
