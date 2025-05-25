# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 07:21:49 2018

@author: srikant nayak
"""

import scipy.fftpack
import cv2
import numpy as np

camera_man=cv2.imread('cameraman.tif')
hori=cv2.imread('horiz.png')
vert=cv2.imread('vertical.png')
x=scipy.fftpack.dct(camera_man)
scipy.misc.imsave('dct_cam.jpg',x)
y=scipy.fftpack.dct(hori)
scipy.misc.imsave('dct_hor.jpg',y)
z=scipy.fftpack.dct(vert)
scipy.misc.imsave('dct_vert.jpg',z)
from matplotlib import pyplot as plt
img = cv2.imread('dct_hor.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()