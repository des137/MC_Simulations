# Simulates Ising model using Monte Carlo techniques
# By Amol Deshmukh, The City College of New York, May 2018

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# To create an animation of the Ising model:
import matplotlib.animation as animation

# System parameters
N     = 20		# Number of lattice sites
N_sim = 10000	# Simulation steps
beta  = 0.01 	# Temperature

# Total energy of the system
def energy(state):
	energy=0
	for i in range(N-1):
		for j in range(N-1):
			energy+=-state[i,j]*(state[i+1,j]+state[i,j+1]) 	
	for i in range(N-1):						# Periodic boundary conditions
		energy+=-state[i,N-1]*(state[i+1,N-1]+state[i,0]) 
	for i in range(N-1):						# Periodic boundary conditions
		energy+=-state[N-1,i]*(state[N-1,i+1]+state[0,i])
	energy+=-state[N-1,N-1]*(state[N-1,0]+state[0,N-1])		# Last entry in the matrix
	return energy	


def update(state):
	for _ in range(N_sim):
		old_state=state
		old_ene = energy(old_state)
		i = np.random.randint(N)
		j = np.random.randint(N)
		state[i,j] = (-1)*state[i,j]
		new_ene = energy(state)
		delta_E=new_ene-old_ene
		if delta_E>0 or np.exp(-beta*delta_E)<np.random.uniform(0,1):
			state[i,j] = (-1)*state[i,j]

# Intial state
state = 2*np.random.randint(2, size=(N,N))-1
# Monte Carlo updates
update(state)

# Snapshot of the Ising model
plt.imshow(state, interpolation='nearest')
plt.gray()
plt.show()

exit()
