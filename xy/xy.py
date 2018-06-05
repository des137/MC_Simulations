# Animation of XY model using Monte Carlo techniques
# By Amol Deshmukh and Areg Ghazaryan, The City College of New York, June 2018

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm

# Initial parameters
N        = 20         # Size of the lattice
N_sweeps = 10**(4)    # Number of sweeps = number of frames
nd       = 10**(-6)   # Delay between frames in miliseconds
temp     = 10**(-1)   # Tempearature

# Initial random state
x, y = np.meshgrid(np.arange(0, 2,.2),np.arange(0,2,.2))

u=np.zeros(100)
for i in range(100):
    u[i]=2*np.random.random()-1

plt.figure()

state = plt.quiver(x,y,u,v)#, units='width')

plt.xlim(-0.2,2)
plt.ylim(-0.2,2)
plt.show()

'''
state = 2 * np.random.randint(2, size = (N, N)) - 1

# Frame set-up
fig = plt.figure(frameon = False)
im = plt.imshow(state, extent=(0, N, 0, N), #interpolation = 'none', 
	animated = True, cmap = cm.binary)

# Energy of the state
def total_energy(state):
    energy_val = 0
    for i in range(N):
        for j in range(N):
            energy_val += 
    return energy_val       

# Local energy change of the system after a spin flip
def diff_energy(state,i,j):
    return 

# Monte Carlo updates
def update(frame): # *args):

# Animate
ani = animation.FuncAnimation(fig, update, frames = N_sweeps, interval = nd, blit = True, repeat = False)

plt.show()
'''