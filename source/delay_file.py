
'''Define function for selecting no.s from given probability distribution'''
import input_file
import numpy as np
from numpy.random import choice
def delay_(max_delay=input_file.nlevels,prob_dist=input_file.prob_set):
    allowed_delays=np.arange(0.,max_delay)
    delay_chosen=choice(allowed_delays,p=prob_dist)
    return delay_chosen


'''
Testing 
x=0
for i in range(10000):
    x+=delay_(6)
print(x/10000)

'''

