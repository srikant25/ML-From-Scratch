# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 15:28:09 2018

@author: srikant nayak
"""


import numpy as np
import csv
def normalization(my_data):
    std_dev=np.std(my_data,axis=0,dtype=float)
    mean=np.mean(my_data,axis=0,dtype=float)
    zscore =(my_data - mean)/std_dev
    return zscore
