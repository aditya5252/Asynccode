
import numpy as np
# number of grid points/ elements
Nx=256
# cfl number
cfl=0.08
# simulation end time
tend=0.5
# convective velocit(ies)
c=1.0
# diffusivity constant
eta=0.1
# number of wavenumbers
numk=3
# wavenumbers
k_ls=np.array([2,1,2])
# amplitudes
amp_ls=np.array([4,2,2])
# number of phase angles
numphi=1
# phase angles
phi_ls=np.array([0])
# number of PEs
numPE=4
# nlevels
nlevels=4
# number of sets
nsets=1
# probability for each set
prob_set=[0.3,0.5,0.2,0.0]

