# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 01:13:49 2018

@author: SRIKANT
"""

import numpy
from skimage import io,color
from PIL import Image , ImageFilter
from scipy import fftpack

c=ImageFilter.Kernel((3,3),numpy.ones(9)*1/9)
c=color.rgb2gray(img)
p=fftpack.fft2(img)
print(p)