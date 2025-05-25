# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:15:18 2018

@author: srikant nayak
"""


import numpy as np
import math
from gd_steepest import gradient_descent
from zs import normalization
my_data=np.genfromtxt('Data1.txt',delimiter=',')
print(my_data)