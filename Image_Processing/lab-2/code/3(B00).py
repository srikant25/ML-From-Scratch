# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 23:52:57 2018

@author: SRIKANT
"""

from PIL import Image,ImageFilter
import numpy as np
img = Image.open('cameraman.tif')
c=ImageFilter.Kernel((3,3),np.ones(9)*1/9)
img.save('camera.png')