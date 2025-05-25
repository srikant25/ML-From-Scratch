# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 22:45:55 2018

@author: srikant nayak
"""


from PIL import Image
import numpy as np
from matplotlib import pyplot as plt



def FFT(A):

    f = np.fft.fft2(A)
    fshft = np.fft.fftshift(f)
    Mag_Spect = 20*np.log(np.abs(fshft))

    plt.subplot(121),plt.imshow(A, cmap = 'gray')
    plt.title('Input Image')
    plt.subplot(122),plt.imshow(Mag_Spect, cmap = 'gray')
    plt.title('Magnitude Spectrum') 
    return;


cman = Image.open('D:/ml lab prog/dip/lab 4/cameraman.tif').convert('L')
FFT(cman)

hor3 = Image.open('D:/ml lab prog/dip/lab 4/hor3.png').convert('L')
FFT(hor3)

hor4 = Image.open('D:/ml lab prog/dip/lab 4/hor4.png').convert('L')
FFT(hor4)

hor5 = Image.open('D:/ml lab prog/dip/lab 4/hor5.gif').convert('L')
FFT(hor5)

hor6 = Image.open('D:/ml lab prog/dip/lab 4/hor6.png').convert('L')
FFT(hor6)

horiz = Image.open('D:/ml lab prog/dip/lab 4/horiz.png').convert('L')
FFT(horiz)

verical = Image.open('D:/ml lab prog/dip/lab 4/vertical.png').convert('L')
FFT(verical)

vertical2 = Image.open('D:/ml lab prog/dip/lab 4/vertical2.jpg').convert('L')
FFT(vertical2)

vert3 = Image.open('D:/ml lab prog/dip/lab 4/vert3.png').convert('L')
FFT(vert3)
