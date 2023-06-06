import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import sklearn.datasets
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
x = np.array([3,5,10,13])
y = np.array([25,58,89,147])

A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
sns.lineplot(x=x,y=y)

def simple_linear_regression(x,y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m,c

ds = clear_data_home
scaler = StandardScaler().fit(x_train)











































# df = pd.read_csv('gene_expression.csv')
#
# x = df['Gene One']
# y = df['Gene Two']
# sb.scatterplot(data = df ,x = x , y = y)
# plt.show()
