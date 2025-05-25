# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 06:48:19 2018

@author: srikant nayak
"""

from scipy import signal,misc

import numpy as np
from PIL import Image
import cv2

def avg_filt(dim):
   h=list()
   if dim==3 or dim==5 or dim==11:
       for i in range(dim):
           for j in range(dim):
               h.append(1/9)
       h=np.asarray(h)
       y=np.reshape(h,(dim,dim))
       r=signal.convolve2d(im,y)
       img=Image.fromarray(r)
       misc.imsave('avg_filter{0}.png'.format(dim),img)

im=cv2.imread('avg.png',0)
avg_filt(int(input('enter the filter dimension 3 or 5 or 11')))