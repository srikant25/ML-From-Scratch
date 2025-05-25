# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 19:21:44 2018

@author: SRIKANT
"""




import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,5,6,3,2,1,1,1])
p=x*2

n=np.arange(0,len(x))



plt.stem(n,p)