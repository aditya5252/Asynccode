import numpy as np

def error_MSE_(x,y):
    if(len(x)!=len(y)):
        return 'Incorrect shapes'
    err=np.absolute(np.subtract(x, y)).mean()
    return err