# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 03:23:11 2018

@author: srikant nayak
"""

import numpy as np
from PIL import Image
from scipy.misc import imsave
from skimage.util import random_noise
img=Image.open('cameraman.tif').convert('L')
img_arr=np.array(img)
ims=random_noise (img_arr,mode='')
imsave('noise1.png',ims)



'''
row,col= img_arr.shape
mean = 1
var = 2
sigma = var**0.5
gauss = np.random.normal(mean,sigma,(row,col))
gauss_noisy=Image.fromarray(gauss)

gauss = gauss.reshape(row,col)
noisy = img + gauss
ima_noisy=Image.fromarray(noisy)
ima_noisy.show()
ima_noisy.save('gaussian.png')
'''