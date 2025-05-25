# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:41:09 2018

@author: SRIKANT
"""

import numpy as np
def normalization(my_data):
   
    my_data =np.genfromtxt(my_data,delimiter=',')
    rows=my_data.shape[0]
    column=my_data.shape[1]
    mean=np.mean(my_data,axis=1,dtype=float)
    std_dev=np.std(my_data,axis=1,dtype=float)
    z_score=np.zeros(my_data.shape,dtype=float)   
        
    i=0
    for i in range(rows):
        for j in range(column):
            z_score[i][j] =(np.subtract(my_data[i][j],mean[j]))/std_dev[j]
    return(z_score)       

x=normalization('Data2.csv')
print(x)



            

