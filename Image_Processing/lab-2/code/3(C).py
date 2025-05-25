# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 00:20:44 2018

@author: SRIKANT
"""


from skimage import io , color
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from PIL import Image
img=io.imread("cameraman.tif")
img=color.rgb2gray(img)
h=np.array([[0,-1,0], [-1,4,-1], [0,-1,0]])
y=signal.convolve2d(img,h,'valid')
y=color.gray2rgb(y)
plt.imshow(y)