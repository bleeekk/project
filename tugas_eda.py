# -*- coding: utf-8 -*-
"""Tugas EDA

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r-yX3UieDe0RR1uivhkbe9H0TMeWuAe-
"""

import numpy as np
import pandas as pd
pd.plotting.register_matplotlib_converters()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
sns.set(style='whitegrid')

data = pd.read_csv('classification.csv')

data.head()

data['success'].value_counts()

data.shape

data.info()

data.describe()

"""###Unvariate Analysis"""

data['success'].unique()

sukses = data.loc[data['success']== 1.0]
tidak_sukses = data.loc[data['success'] == 0.0]

data.columns

#mengatur subplots
f,axes = plt.subplots(ncols=2,nrows=2,figsize=(10,10),sharex=True)
l=['age', 'interest']
for i in range(2):
  #menggambar boxplot
  sns.boxplot(x = data.loc[:,l[i]], ax=axes[i][0], color='powderblue')

  #menggambar KDE
  sns.histplot(data = data.loc[:,l[i]], color='red', kde=True, stat='density', linewidth=0, ax=axes[i][1])

  plt.tight_layout()

"""### Bivariate Data Analysis"""

f,axes = plt.subplots(ncols=1, figsize=(5,5),sharex=True)
sns.despine(left=True) #age vs success


sns.histplot(data=sukses['age'],label='1,0',color='b',kde=True,linewidth=2,alpha=0.3)
sns.histplot(data=tidak_sukses['age'],label='0,0',color='orange',kde=True,linewidth=2,alpha=0.3)

plt.legend()
plt.tight_layout()

f,axes = plt.subplots(ncols=1, figsize=(5,5),sharex=True)
sns.despine(left=True) #interest vs success


sns.histplot(data=sukses['interest'],label='1,0',color='b',kde=True,linewidth=2,alpha=0.3)
sns.histplot(data=tidak_sukses['interest'],label='0,0',color='orange',kde=True,linewidth=2,alpha=0.3)

plt.legend()
plt.tight_layout()

sns.pairplot(data,hue='success',diag_kind='hist')
plt.show()

"""###Swarm plot dan Box plot"""

f,axes = plt.subplots(ncols=2, figsize=(10,5),sharex=True)
sns.despine(left=True)

sns.swarmplot(x=data['success'],y=data['age'],ax=axes[0])

sns.boxplot(x=data['success'],y=data['age'],ax=axes[1])
plt.tight_layout()