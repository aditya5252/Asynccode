import numpy as np
import probability_initial
import delay_file
    
def at2u0(pe,l,L, p_arr):   
    a = l+1 
    b = -l 
    temp = a*p_arr[int(L-1-l)][int(pe)]+b*p_arr[int(L-2-l)][int(pe)]
    return temp


def cd2u1(u,cx,dx,nx,Eqflag,Syncflag,L=None,PE=None,perPE=None,pstart=None,pend=None,ATolFLAG=None):
    '''For a given time step t to t+delt'''
#     u,du,C all take 1-D
    rhs=np.zeros_like(u)
    C=np.zeros_like(u)
    '''Concentration array'''
    if(Eqflag=='DBurgers'):
        C=u.copy()
    if((Eqflag=='DAdvection') or (Eqflag=='DAD')):
        for i in range(nx):
            C[i]=cx

    if(Syncflag=='DSync'):
        rhs[0] = -C[0]*(u[1] - u[nx-2])/(2*dx)
        rhs[nx-1] = -C[nx-1]*(u[1] - u[nx-2])/(2*dx)
        for i in range(1,nx-1):
            rhs[i] = -C[i]*(u[i+1] - u[i-1])/(2*dx)
        return rhs
            
    elif(Syncflag=='DAsync'):
        ## Interior point computations ##
        for pe in range(PE):       
            for i in range(pe*perPE+1,perPE*(pe+1)-1):
                rhs[i] = -C[i]*(u[i+1] - u[i-1])/(2*dx)
                
        ## Assigning values to buffer array ##
        #L=max_delay

       ## pend with left_pt    &   pstart with right_pt ##
        #Different l use        
        if(ATolFLAG==None):
            l=int(delay_file.delay_())
            rhs[0] = -C[0]*(u[1] - pend[L-1-l][PE-1])/(2*dx)
            l=int(delay_file.delay_())
            rhs[nx-1] = -C[nx-1]*(pstart[L-1-l][0*PE]- u[nx-2])/(2*dx)
            #Processor Boundary points
            for pe in range(PE-1):
                right_pt = perPE*(pe+1)-1
                l=int(delay_file.delay_())
                rhs[right_pt] = -C[right_pt]*(pstart[L-1-l][(right_pt+1)//perPE] - u[right_pt-1])/(2*dx)
                l=int(delay_file.delay_())
                left_pt = perPE*(pe+1)
                rhs[left_pt] = -C[left_pt]*(u[left_pt+1] - pend[L-1-l][(left_pt+1)//perPE - 1])/(2*dx)
        elif(ATolFLAG=='DAT2'):
            l=int(delay_file.delay_())
            rhs[0] = -C[0]*(u[1] - at2u0(PE-1,l,L,pend) )/(2*dx)
            l=int(delay_file.delay_())
            rhs[nx-1] = -C[nx-1]*( at2u0(0,l,L,pstart) - u[nx-2] )/(2*dx)
            #Processor Boundary points
            for pe in range(PE-1):
                right_pt = perPE*(pe+1)-1
                l=int(delay_file.delay_())
                rhs[right_pt] = -C[right_pt]*( at2u0((right_pt+1)/perPE,l,L,pstart)- u[right_pt-1])/(2*dx)
                l=int(delay_file.delay_())
                left_pt = perPE*(pe+1)
                rhs[left_pt] = -C[left_pt]*(u[left_pt+1] - at2u0((left_pt+1)//perPE - 1,l,L,pend))/(2*dx)
        pstart_out=pstart[1:]
        pend_out=pend[1:]
        
        return rhs,pstart_out,pend_out

def euler(u,rhs,dt,nx):
#     v=np.zeros_like(u)
#     for i in range(nx):
#         v[i]=u[i]+dt*rhs[i]
    u=u+dt*rhs
    return u

# import numpy as np
# import probability_initial
# import delay_file
# def cd2u1(u,cx,dx,nx,Eqflag,Syncflag,L=None,PE=None,perPE=None,pstart_in=None,pend_in=None):
#     '''For a given time step t to t+delt'''
# #     u,du,C all take 1-D
#     rhs=np.zeros_like(u)
#     C=np.zeros_like(u)
#     '''Concentration array'''
#     if(Eqflag=='DBurgers'):
#         C=u.copy()
#     if((Eqflag=='DAdvection') or (Eqflag=='DAD')):
#         for i in range(nx):
#             C[i]=cx

#     if(Syncflag=='DSync'):
#         rhs[0] = -C[0]*(u[1] - u[nx-2])/(2*dx)
#         rhs[nx-1] = -C[nx-1]*(u[1] - u[nx-2])/(2*dx)
#         for i in range(1,nx-1):
#             rhs[i] = -C[i]*(u[i+1] - u[i-1])/(2*dx)
#         return rhs
            
#     elif(Syncflag=='DAsync'):
#         ## Interior point computations ##
#         for pe in range(PE):       
#             for i in range(pe*perPE+1,perPE*(pe+1)-1):
#                 rhs[i] = -C[i]*(u[i+1] - u[i-1])/(2*dx)
                
#         ## Assigning values to buffer array ##
#         #L=max_delay
#         pstart=np.zeros((L,PE))
#         pend=np.zeros((L,PE))

#         pstart[:-1]=pstart_in
#         pend[:-1]=pend_in
        
#         pstart[L-1],pend[L-1]=probability_initial.prob_1D_from_u_1D(u,PE,perPE)
#        ## pend with left_pt    &   pstart with right_pt ##
#         #Different l use        
#         l=int(delay_file.delay_())
#         rhs[0] = -C[0]*(u[1] - pend[L-1-l][PE-1])/(2*dx)
#         l=int(delay_file.delay_())
#         rhs[nx-1] = -C[nx-1]*(pstart[L-1-l][0*PE]- u[nx-2])/(2*dx)
#         #Processor Boundary points
#         for pe in range(PE-1):
#             right_pt = perPE*(pe+1)-1
#             l=int(delay_file.delay_())
#             rhs[right_pt] = -C[right_pt]*(pstart[L-1-l][(right_pt+1)//perPE] - u[right_pt-1])/(2*dx)
#             l=int(delay_file.delay_())
#             left_pt = perPE*(pe+1)
#             rhs[left_pt] = -C[left_pt]*(u[left_pt+1] - pend[L-1-l][(left_pt+1)//perPE - 1])/(2*dx)
        
#         pstart_out=pstart[1:]
#         pend_out=pend[1:]
        
#         return rhs,pstart_out,pend_out

# def euler(u,rhs,dt,nx):
# #     v=np.zeros_like(u)
# #     for i in range(nx):
# #         v[i]=u[i]+dt*rhs[i]
#     u=u+dt*rhs
#     return u