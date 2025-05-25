# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:21:11 2018

@author: srikant nayak
"""
from PIL import Image
import scipy.misc
import numpy as np
from matplotlib import pyplot as plt

cameraman=Image.open('cameraman.tif')
hor=Image.open('horiz.png')
vert=Image.open('vertical.png')

camera=abs(np.fft.fft2(cameraman))
np.fft.fftshift(camera)
scipy.misc.imsave('cameraman.jpg', camera)

horiz=abs(np.fft.fft2(hor))
np.fft.fftshift(horiz)
scipy.misc.imsave('horizontal.jpg', horiz)


ver=abs(np.fft.fft2(vert))
np.fft.fftshift(ver)
scipy.misc.imsave('verti.jpg', ver)




img = Image.open('cameraman.jpg',0)
fig = np.fft.fft2(img)
fshift = np.fft.fftshift(fig)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


img = Image.open('horizontal.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


img = Image.open('verti.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()