# -*- 1-d convolution-*-
"""
Created on Sun Aug 19 19:28:51 2018

@author: SRIKANT
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,1,1,1,1])
h=np.array([0,0,1,1,1,1,1,1,0])
convolution=np.convolve(x,h)
print(convolution)
plt.stem(convolution)