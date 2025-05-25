# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 21:56:55 2018

@author: SRIKANT
"""


import numpy as np
import matplotlib.pyplot as mpl

array1 =np.array([1,2,1.3,1.4,5])  
mpl.plot(array1,label='Original')
array2= np.convolve(array1,array1)
mpl.plot(array2,label='self Convolution 1')
array3= np.convolve(array2,array2)
mpl.plot(array3,label='self Convolution 2')           
mpl.legend()
      