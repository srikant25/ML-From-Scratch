# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 01:02:27 2018

@author: SRIKANT
"""

import numpy as np
from skimage import io,color
import matplotlib.pyplot as plt
from scipy import fftpack
img=io.imread('cameraman,tif')
img=color.rgb2gray(img)
p=fftpack.fft2(img)
mag_spect = 20*np.log(np.abs(p))
plt.plot(mag_spect)