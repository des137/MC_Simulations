# Animation of Ising model using Monte Carlo techniques
# By Amol Deshmukh and Areg Ghazaryan, The City College of New York, June 2018

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm

#Changes:I replaced two varibales Nx,Ny with a single variable N, since we'll simulate square ising model

# Initial parameter
N        = 100
N_sweeps = 10**(4)    # Number of sweeps = number of frames
nd       = 10**(-6)   # Delay between frames in miliseconds
temp     = 0.1
expar = np.array([np.exp(-4.0 / temp), np.exp(-8.0 / temp)])
counter = 0
randm = 1000
randa = np.random.randint(N, size = randm)

# Initial random state
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
            energy_val += -state[i,j]*(state[(i+1)%N,j]+state[i,(j+1)%N])
    return energy_val       

# Local energy change of the system after a spin flip
def diff_energy(state,i,j):
    return 2*state[i,j]*(state[(i-1)%N,j]+state[i,(j-1)%N]+state[(i+1)%N,j]+state[i,(j+1)%N])   

# Monte Carlo updates
def update(frame): # *args):
    global counter
    global randa
    if counter == randm :
        randa = np.random.randint(N, size = randm)
        counter = 0
    i = randa[counter]
    j = randa[counter + 1]
    counter += 2
    nnsum = state[(i-1)%N,j]+state[i,(j-1)%N]+state[(i+1)%N,j]+state[i,(j+1)%N]
    if state[i, j] < 0:
        if nnsum >= 0 or expar[-nnsum // 2 - 1] > np.random.uniform(0,1):
            state[i,j] *= -1
    else:
        if nnsum <= 0 or expar[nnsum // 2 - 1] > np.random.uniform(0,1):
            state[i,j] *= -1
    im.set_data(state)
    return im,

# Animate
ani = animation.FuncAnimation(fig, update, frames = N_sweeps, interval = nd, blit = True, repeat = False)

plt.show()
