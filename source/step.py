import numpy as np
def cd2u1(u,cx,dx,nx,Eqflag,Syncflag,L=None,PE=None,perPE=None):
    '''For a given time step t to t+delt'''
#     u,du,C all take 1-D
    rhs=np.zeros_like(u)
    C=np.zeros_like(u)
    '''Concentration array'''
    if(Eqflag=='DBurgers'):
        C=u
    if((Eqflag=='DAdvection') or (Eqflag=='DAD')):
        for i in range(nx):
            C[i]=cx

    if(Syncflag=='DSync'):
        rhs[0] = -C[0]*(u[1] - u[nx-2])/(2*dx)
        rhs[nx-1] = -C[nx-1]*(u[1] - u[nx-2])/(2*dx)
        for i in range(1,nx-1):
            rhs[i] = -C[i]*(u[i+1] - u[i-1])/(2*dx)
    return rhs

def euler(u,rhs,dt,nx):
#     v=np.zeros_like(u)
#     for i in range(nx):
#         v[i]=u[i]+dt*rhs[i]
    u=u+dt*rhs
    return u