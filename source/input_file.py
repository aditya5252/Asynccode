
import numpy as np
# number of grid points/ elements
Nx=256
# cfl number
cfl=0.08
# simulation end time
tend=0.5
# simulation time-steps
N_t_=15
# convective velocit(ies)
c=1.0
# diffusivity constant
eta=0.1
# number of wavenumbers
numk=1
# wavenumbers
k_ls=np.array([1.])
# amplitudes
amp_ls=np.array([1.])
# number of phase angles
numphi=1
# phase angles
phi_ls=np.array([0.])
# number of PEs
numPE=4
# nlevels
nlevels=3
# number of sets
nsets=1
# probability for each set
prob_set=[0.3,0.5,0.2]

