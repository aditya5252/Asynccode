
import numpy as np
def analytical_(x,amp,kappa,phi,num_k,num_phi,Nx,tend,cx,nu):
    u=np.zeros(Nx)
    for i in range(Nx):
        for k1 in range(num_k):
            for k2 in range(num_phi):
                u[i]+= amp[k1]*np.exp(-kappa[k1]*kappa[k1]*nu*tend)*np.sin(kappa[k1]*(x[i]-cx*tend)+phi[k2])
    return u

