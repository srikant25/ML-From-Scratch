# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 23:23:04 2018

@author: SRIKANT
"""


import matplotlib.pyplot as plt
import numpy as np
p=list()
q=list()
r=list()
for i in range(0,8):
    p.append((0.5)**i)
    q=[0,0,0,1,1,1,1]
    r=[1,-1]
plt.subplot(221)
plt.stem(p)
plt.subplot(p)
plt.subplot(222)
plt.stem(q)
plt.ylabel(q)
plt.subplot(223)
plt.stem(r)
plt.ylabel(r)
z=np.convolve(p,q)
z=np.convolve(z,r)
plt.subplot(224)
plt.stem(z)
plt.ylabel(z)