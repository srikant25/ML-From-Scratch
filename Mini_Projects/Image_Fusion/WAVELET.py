# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:38:40 2018

@author: srikant nayak
"""

from PIL import Image
import pywt
import numpy as np
import matplotlib.pyplot as plt
img1 = Image.open('s1.gif').convert('L')
img2 = Image.open('ss2.gif').convert('L')
img1_ary = np.array(img1)
img2_ary = np.array(img2)
import pywt
coeff1  = pywt.dwt2(img1_ary,wavelet='haar')
coeff2  = pywt.dwt2(img2_ary,wavelet='haar')
LL1, (LH1, HL1, HH1) = coeff1
LL2,(LH2,HL2,HH2 ) = coeff2
def fuse_coeff(coeff1, coeff2):
   coeff = (coeff1 + coeff2) / 2
   return coeff
fusedCooef = []
for i in range(len(coeff2)-1):
   if(i == 0):
       fusedCooef.append(fuse_coeff(LL1,LL2))
   else:
       c1 = fuse_coeff(coeff1[i][0], coeff2[i][0])
       c2 = fuse_coeff(coeff1[i][1], coeff2[i][1])
       c3 = fuse_coeff(coeff1[i][2], coeff2[i][2])

       fusedCooef.append((c1,c2,c3))
fusedImage = pywt.waverec2(fusedCooef, wavelet='haar')
plt.imshow(fusedImage)#,cmap='gray')