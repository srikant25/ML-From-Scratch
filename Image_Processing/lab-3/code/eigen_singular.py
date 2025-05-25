# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:41:22 2018

@author: srikant nayak
"""

import numpy as np
from numpy import linalg as LA
array=[[1,0,1],[0,1,1],[0,0,0]]
a=np.array(array)
eigen_value,eigen_vector = LA.eig(a)
print(eigen_value)
ata=np.dot(a.T,a)
eigen_value2,eigen_vector2 = LA.eig(ata)
print(eigen_value2)
x=np.shape(eigen_value2)
for i in range(len(x)):
    singular_value=np.sqrt(eigen_value[i])
    print(singular_value)


