# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:27:32 2018

@author: srikant nayak
"""

def discretize(X,k,size):
    
    import pandas as pd
    df[k] = pd.cut(X[k],size)
    df[k] = df[k].apply(lambda x: x.mid).astype('float64')

#df=pd.read_csv('wdbcdata.csv')

for k in df.iloc[:,:-1].columns:
   discretize(df,k,5)