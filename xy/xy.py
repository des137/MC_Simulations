# Simulates XY model using Monte Carlo techniques
# By Amol Deshmukh and Areg Ghazaryan, The City College of New York, June 2018

import numpy as np
import matplotlib.pyplot as plt

# System parameters
N        = 20               # Number of lattice sites
N_sweeps = 15*10**5         # Number of Monte Carlo sweeps
temp     = 0.05            # Temperature
eps      = 0.1				# Small deviation

# Total energy of a configuration
def total_energy(state):
	energy=0
	for i in range(N):
		for j in range(N):
			energy+=np.cos(state[i,j]-(state[(i+1)%N,j])+np.cos(state[i,j]-state[i,(j+1)%N]))
	return energy		

# Local energy change in the system after a spin flip
def diff_energy(state,i,j):
	return (np.cos((eps+state[i,j])-state[(i-1)%N,j])
		+np.cos((eps+state[i,j])-state[i,(j-1)%N])
		+np.cos((eps+state[i,j])-state[(i+1)%N,j])
		+np.cos((eps+state[i,j])-state[i,(j+1)%N]))
	-((np.cos((state[i,j])-state[(i-1)%N,j])
		+np.cos((state[i,j])-state[i,(j-1)%N])
		+np.cos((state[i,j])-state[(i+1)%N,j])
		+np.cos((state[i,j])-state[i,(j+1)%N]))) 	

# Monte Carlo update	
def update(state):
	energy[0]        = total_energy(state)                             # Energy of the initial state
	magnetization[0] = state.sum()                                     # Magnetization of the initial state
	for k in range(N_sweeps):		
		i = np.random.randint(N)
		j = np.random.randint(N)
		delta_E = diff_energy(state,i,j)                               # Change in energy
		if delta_E<0 or np.exp(-delta_E/temp)>np.random.uniform(0,1):
			state[i,j] += eps                                          # Metropolis step
			magnetization[k] = magnetization[k-1]+2*state[i,j]
			energy[k]        = energy[k-1]+delta_E
		else: 
			magnetization[k] = magnetization[k-1]
			energy[k]        = energy[k-1]

# Intial state
state = 2*np.pi*np.random.random((N,N))

# Magnetization/energy value holder
magnetization = np.zeros(N_sweeps)
energy        = np.zeros(N_sweeps)

# Monte Carlo updates
update(state)

# Snapshot of the configuration at the end of Monte Carlo simulation
plt.imshow(state)
plt.title('Final configuration of the Ising model')
#plt.gray()
plt.show()

# Net Magnetization as a functions of number of Monte Carlo sweeps
plt.plot(magnetization)
plt.xlabel('Number of sweeps')
plt.ylabel('Net Magnetization')
plt.ylim(-1.1*N**2,1.1*N**2)
plt.grid(True)
plt.show()

# Net Magnetization as a functions of number of Monte Carlo sweeps
plt.plot(energy)
plt.xlabel('Number of sweeps')
plt.ylabel('Total Energy')
plt.grid(True)
plt.show()

# Histogram for 'Net Magnetization'
plt.hist(magnetization,bins=100)
plt.xlim(-1.1*N**2,1.1*N**2)
plt.xlabel('Net Magnetization')
plt.ylabel('Counts')
plt.show()

exit()