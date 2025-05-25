# -*- normalization/min-max-*-
"""
Created on Sat Aug 18 10:03:57 2018

@author: SRIKANT
"""

import numpy as np
import pandas as pd

my_data=np.genfromtxt('Data2.csv',delimiter=',')
df=pd.read_csv('Data2.csv',header=None)
minimum=np.amin(my_data,axis=0)
maximum=np.amax(my_data,axis=0)
normal=np.zeros(df.shape,dtype=float)

rows=df.shape[0]
column=df.shape[1]
i=0
for j in range(column):
    for i in range(rows):
        normal[i][j]=(np.subtract(my_data[i][j],minimum[j]))/(np.subtract(minimum[j],maximum[j]))
        
       
        
print(normal)
        
        
        
        