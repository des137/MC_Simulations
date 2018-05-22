# Simulates Ising model using Monte Carlo techniques
# By Amol Deshmukh, The City College of New York, May 2018

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# To create an animation of the Ising model:
import matplotlib.animation as animation

# System parameters
N   = 50	# Number of lattice sites
beta= 1.0 	# Temperature

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

#Intial state
# ground_state = np.ones((N,N))
state = 2*np.random.randint(2, size=(N,N))-1

# Store an old state 
old_state = state
old_ene = energy(old_state)
old_exp = np.exp(-beta*energy(old_state))

# An update on the initial state by a spin flip
i = np.random.randint(N)
j = np.random.randint(N)
state[i,j] = (-1)*state[i,j]
new_ene = energy(state)
new_exp = np.exp(-beta*energy(state))

print("Total energy is", old_ene, "units")
print("Total energy is", new_ene, "units")

print(old_exp>new_exp)

# Snapshot of the Ising model
plt.imshow(state, interpolation='nearest')
plt.gray()
plt.show()

exit()

# Animation of the monte carlo sweeps
