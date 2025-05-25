# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 08:59:02 2018

@author: SRIKANT
"""

import numpy
import scipy
from skimage import io,color
import matplotlib.pyplot as plt
from PIL import Image , ImageFilter
from scipy import fftpack
img=io.imread('cameraman.tif')
c=ImageFilter.Kernel((3,3),numpy.ones(9)*1/9)
c=color.rgb2gray(img)
p=fftpack.fft2(c)

img=color.rgb2gray(img)
q=fftpack.fft2(img)
mul=p*q
print(mul)
inverse=scipy.fftpack.ifft(mul)
print(inverse)