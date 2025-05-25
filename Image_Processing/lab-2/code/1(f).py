# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 19:26:11 2018

@author: SRIKANT
"""




import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,5,6,3,2,1,1,1])
n=np.arange(0,len(x))
n=n*3

plt.stem(n,x)
