# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 00:13:53 2018

@author: srikant nayak
"""

import scipy.fftpack
import cv2
from matplotlib import pyplot as plt
import numpy as np

camera_man=cv2.imread('cameraman.tif')
horizontal=cv2.imread('horiz.png')
vertical=cv2.imread('vertical.png')

x=scipy.fftpack.dct(camera_man)
scipy.misc.imsave('dct_camera.jpg',x)

y=scipy.fftpack.dct(horizontal)
scipy.misc.imsave('dct_horizontal.jpg',y)

z=scipy.fftpack.dct(vertical)
scipy.misc.imsave('dct_vertical.jpg',z)
img = cv2.imread('dct_horizontal.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()