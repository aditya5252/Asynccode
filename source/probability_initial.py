
import numpy as np

def prob_1D_from_u_1D(u,PE,perPE):
    pstart=np.zeros(PE)
    pend=np.zeros(PE)
    for pe in range(PE-1):
        pstart[pe+1]=u[(pe+1)*perPE]
        pend[pe]=u[(pe+1)*perPE-1]
        #Periodic Boundary points
    pstart[0]=u[0*perPE +1]
    pend[PE-1]=u[(PE)*perPE-1-1]
    
    return pstart,pend

def prob_2D_from_arr_2D(arr2D,PE,perPE,m):
    # m = L-1 steps
    if (m!=arr2D.shape[0]):
        print('ERROR : Shapes not compatible')
        return
    prob_S_list,prob_E_list=[],[]
    for i in range(m):
        ps,pe=prob_1D_from_u_1D(arr2D[i],PE,perPE)
        prob_S_list.append(ps)
        prob_E_list.append(pe)
    prob_2D_S_arr=np.stack(prob_S_list)
    prob_2D_E_arr=np.stack(prob_E_list)
    return prob_2D_S_arr,prob_2D_E_arr
        

