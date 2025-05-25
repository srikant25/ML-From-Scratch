# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:15:06 2018

@author: srikant nayak
"""

from skimage import io,color
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy import fftpack
img=Image.open('cameraman.tif').convert('L')
img=color.rgb2gray(img)
p=fftpack.fft2(img)
mag_spectrum = 20*np.log(np.abs(p))
plt.plot(mag_spectrum)

