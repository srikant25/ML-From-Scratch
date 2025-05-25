# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:36:39 2018

@author: srikant nayak
"""

from PIL import Image
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from scipy.linalg import eigh

img1 = Image.open('s1.gif').convert('L')
img2 = Image.open('ss2.gif').convert('L')
i1 = np.array(img1)
i2 = np.array(img2)
img_arry1 = pd.DataFrame(np.array(img1).flatten())
img_ary = pd.DataFrame(np.array(img1).flatten())
img_arry2 = pd.DataFrame(np.array(img2).flatten())
img_ary.insert(1,'',img_arry2)
img_matrix = img_ary
std_data = StandardScaler().fit_transform(img_matrix)
data = np.matmul(std_data.T,std_data)
cov_matrix = np.cov(data)
val,vec = eigh(cov_matrix,eigvals=(1,1)) #std_data.shape (262144, 2)
v=np.sum(vec)
p1 = vec[0] / v
p2 = vec[1] / v
r1 = p1 * i1
r2 = p2 * i2
r = r1 + r2
img = Image.fromarray(r)
import matplotlib.pyplot as plt
plt.subplot(2,2,1),plt.imshow(img1),plt.title('original_image1')
plt.subplot(2,2,2),plt.imshow(img2),plt.title('original_image2')
#plt.imshow(r)#,cmap='gray')
plt.imshow(r)