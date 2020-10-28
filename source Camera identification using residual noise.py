# -*- coding: utf-8 -*-
"""Final model for phase 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MfV8xZofYvkNmLeeWASr7OAv8TPtSEIv
"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

import pandas as pd

dataset2 = pd.read_csv("noise_final_1.csv")

dataset2

df2y = dataset2["camera"]
df2 = dataset2.drop(['camera'], axis = 1) 
df2y = dataset2["camera"].replace('Canon5D2' , 1)

df2y = df2y.replace('canon80D' , 2)
df2y = df2y.replace('nikon800' , 3)
df2y = df2y.replace('sonyA7' , 4)
df2y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df2,df2y, test_size = 0.2)

from sklearn.svm import SVC

svm = SVC()

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score as acc
from mlxtend.feature_selection import SequentialFeatureSelector as sfs

sfs1 = sfs(svm,
           k_features=50,
           forward=True,
           floating=False,
           verbose=2,
           cv=10)

sfs1 = sfs1.fit(X_train, y_train)

from sklearn.linear_model import LogisticRegression

lreg = LogisticRegression(multi_class = 'multinomial', max_iter = 10000)

sfs1 = sfs(lreg,
           k_features=5,
           forward=True,
           floating=False,
           verbose=2,
           cv=10)

sfs1 = sfs1.fit(X_train, y_train)



"""---------> Here, we test the sfs model on neural networks. #########"""















