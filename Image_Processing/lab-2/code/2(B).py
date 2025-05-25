# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 23:00:30 2018

@author: SRIKANT
"""

import numpy as np
import matplotlib.pyplot as plt
import math

n=np.array([0,1,2,3,4,5])
x=np.array([1 for i in range(0,len(n))],dtype=float)
h=np.array([1 for j in range(0,len(n))],dtype=float)
x=x+4
h=-2-h
for i in range(len(x)):
    n[i]=math.pow(0.5,i)
for j in range(len(h)):
    h[j]=math.pow(4,j)
    convolve=np.convolve(x,h)
plt.stem(convolve)
plt.show()