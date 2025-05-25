# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 23:36:42 2018

@author: SRIKANT
"""

def normalization(my_data):
    import pandas as pd
    df=pd.read_csv('Data2.csv',header=None)
    df1=df.drop(df.columns[len(df.columns)-1],1)
    norm_data=(df1-df1.mean())/df1.std()
    return(norm_data)
    
