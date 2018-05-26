# Simulates Ising model using Monte Carlo techniques
# By Amol Deshmukh, The City College of New York, May 2018

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# To create an animation of the Ising model:
import matplotlib.animation as animation

# System parameters
N     = 20		# Number of lattice sites
N_sim = 300000	# Simulation steps
N_coll= 100	    # Collected steps
T     = 2.2 	# Temperature

# Local energy change of the system after a spin flip
def diff_energy(state,i,j):
	return 2*state[i,j]*(state[(i-1)%N,j]+state[i,(j-1)%N]+state[(i+1)%N,j]+state[i,(j+1)%N]) 	
	
def update(state,counter_coll):
	counter=0
	for _ in range(N_sim):		
		i = np.random.randint(N)
		j = np.random.randint(N)
		delta_E=diff_energy(state,i,j)
		if delta_E<0 or np.exp(-delta_E/T)>np.random.uniform(0,1):
			state[i,j] = (-1)*state[i,j]
		if not counter%N_coll:				
			counter_coll[counter//N_coll]=(state.sum())
		counter+=1	

# Intial state
state = 2*np.random.randint(2, size=(N,N))-1

# Counter of the states
counter_coll=np.zeros(N_sim//N_coll)

# Monte Carlo updates
update(state,counter_coll)

# Snapshot of the Ising model
plt.imshow(state, interpolation='nearest')
plt.gray()

plt.plot(counter_coll)
plt.ylim(-N**2,N**2)
plt.grid(True)
plt.show()

exit()
