
import pandas as pd
import numpy as np
import matplotlib as mat

df = pd.read_csv('Data1.csv',header=None)


def steepest_descent(df,w_exti,alpha,error):
    data = dy=df.iloc[:,-1]
    x=df.iloc[:,:,-1]
    
    