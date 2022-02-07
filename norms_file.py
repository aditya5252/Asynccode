import numpy as np
def v_norm_inf_(arr):
    return abs(arr).max()
def v_norm_1_(arr):
    return ((abs(arr)**1).sum())**(1/1)
def v_norm_n_(arr,n):
    return ((abs(arr)**n).sum())**(1/n)

