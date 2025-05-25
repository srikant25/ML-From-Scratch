# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:57:03 2018

@author: srikant nayak
"""


import numpy as np

my_data=np.genfromtxt('Data4.csv',delimiter=',')

my_data=np.insert(my_data,0,1,axis=1)
x=my_data[0:,0:-1]
y=my_data[:,-1]

w=np.array([0 for i in range(x.shape[1])])
trans = np.dot(x,x.T)
inverse =np.linalg.inv(trans)
trans2=np.dot(x.T,inverse)

w=np.dot(trans2,y)
print(w)