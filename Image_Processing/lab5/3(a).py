# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:31:41 2018

@author: srikant nayak
"""

from PIL import Image

from matplotlib import pyplot as plt
import numpy as np

img = Image.open('cameraman.tif')
img_arr=np.array(img)
w,h=img_arr.shape
for i in range(w):
    for j in range(h):
        plt.hist(img, bins=10, range=None, normed=False, weights=None, density=None)
plt.show()
