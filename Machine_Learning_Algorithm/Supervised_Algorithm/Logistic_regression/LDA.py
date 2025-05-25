# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 01:13:28 2018

@author: srikant nayak
"""
import numpy as np
import scipy

import pandas as pd
df=pd.read_csv('data4.csv',header=None)
label = df.iloc[:,-1]
#norm_data = ( df - df.mean() )/df.std()
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
data = scalar.fit_transform(df)
sample = data
xtx = np.matmul(sample.T,sample)

convolve = np.cov(xtx)

#evalues , evec = scipy.linalg.eigh(cov,eigvals =(191,192))