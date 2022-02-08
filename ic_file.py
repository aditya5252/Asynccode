import numpy as np
def ic_(x,amp,kappa,phi,num_k,num_phi,Nx):
    u=np.zeros(Nx)
    for i in range(Nx):
        for k1 in range(num_k):
            for k2 in range(num_phi):
                u[i]+= amp[k1]*np.sin(kappa[k1]*x[i]+phi[k2])
    return u