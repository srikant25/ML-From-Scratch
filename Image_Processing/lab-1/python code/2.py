# -question 2-*-
"""
Created on Wed Aug 15 22:17:09 2018

@author: SRIKANT
as-
    code 2py
    input_image
    resutl
"""
from PIL import Image
import os
import numpy as np

input_dir='../input_image/'
output_dir='../result/'


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

img=Image.open(input_dir+'lenna.jpg')

print('Image in array form -\n{}'.format(np.array(img)))
img.save(output_dir+'ques-2_lenna.jpg')
print('mode of image : {}'.format(img.mode))
print('size of image: {}'.format(img.size))
print('format of image: {}'.format(img.format))


