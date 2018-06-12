# Animation of XY model using Monte Carlo techniques
# By Amol Deshmukh and Areg Ghazaryan, The City College of New York, June 2018

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm

#Changes:I replaced two varibales Nx,Ny with a single variable N, since we'll simulate square ising model

# Initial parameter
N        = 20
N_sweeps = 10**(4)    # Number of sweeps = number of frames
nd       = 10**(-6)   # Delay between frames in miliseconds
temp     = 0.1

# Intial state
state = 2*np.pi*np.random.random((N,N))

# Frame set-up
fig = plt.figure(frameon = False)
im = plt.imshow(state, extent=(0, N, 0, N), #interpolation = 'none', 
	animated = True)#, cmap = cm.binary)

# Energy of the state
def total_energy(state):
    energy_val = 0
    for i in range(N):
        for j in range(N):
            energy_val += -state[i,j]*(state[(i+1)%N,j]+state[i,(j+1)%N])
    return energy_val       

# Local energy change of the system after a spin flip
def diff_energy(state,i,j,eps):
    return (np.cos((eps-state[i,j])-state[(i-1)%N,j])
        +np.cos((2*eps-state[i,j])-state[i,(j-1)%N])
        +np.cos((2*eps-state[i,j])-state[(i+1)%N,j])
        +np.cos((2*eps-state[i,j])-state[i,(j+1)%N]))
    -((np.cos((2*eps-state[i,j])-state[(i-1)%N,j])
        +np.cos((2*eps-state[i,j])-state[i,(j-1)%N])
        +np.cos((2*eps-state[i,j])-state[(i+1)%N,j])
        +np.cos((2*eps-state[i,j])-state[i,(j+1)%N])))  

# Monte Carlo updates
def update(frame):#, *args):
    i   = np.random.randint(N)
    j   = np.random.randint(N)
    eps = np.random.random() 
    delta_E = diff_energy(state,i,j,eps)                                 # Change in energy
    if delta_E<0 or np.exp(-delta_E/temp)>np.random.uniform(0,1):
        state[i,j] *= -1                                           # Metropolis step
    im.set_data(state)
    return im,

# Animate
ani = animation.FuncAnimation(fig, update, frames = N_sweeps, interval = nd, blit = True, repeat = False)

plt.show()