# ---------Issues----------
# Only shows the last snapshot of the Monte Carlo sweeps

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm 

# Initial parameter
N        = 10    # Size of the lattice
temp     = 1     # Temperature
N_sweeps = 400   # Actual number of sweeps
N_th     = 4     # N^th snapshot 

fig = plt.figure()

# Initial step
state = 2 * np.random.randint(2, size = (N, N)) - 1

# Local energy change of the system after a spin flip
def diff_energy(state,i,j):
    return 2*state[i,j]*(state[(i-1)%N,j]+state[i,(j-1)%N]+state[(i+1)%N,j]+state[i,(j+1)%N])   

# List of images
images = []
for m in range(N_sweeps):
    j=np.random.randint(N-1)
    k=np.random.randint(N-1)
    delta_E = diff_energy(state,j,k)                               # Change in energy
    if delta_E<0 or np.exp(-delta_E/temp)>np.random.uniform(0,1):
        state[j,k] *= -1                                           # Metropolis step
    snapshot = plt.imshow(state)
    images.append([snapshot])

images=images[::N_th]

# Animation
animation.ArtistAnimation(fig, images, interval=50, blit=True, repeat_delay=1000)
plt.show()

exit()
