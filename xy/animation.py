# Animation of XY model using Monte Carlo techniques
# By Amol Deshmukh and Areg Ghazaryan, The City College of New York, June 2018

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial parameters
N         = 20              # Size of the lattice
N_sweeps  = 10**(5)
nd        = 20

# This function calculates the other component of a random vector
def other_comp(U,i,j):
	return (2*np.random.randint(2)-1)*(1-U[i,j]**2)**(1/2)

# Intial x-components of random vectors
U = 2*np.random.rand(N,N)-1    

# Intial y-components of random vectors
V = np.zeros((N,N))
for i in range(len(V)):
	for j in range(len(V)):
		V[i,j] = other_comp(U,i,j)
'''
May need to add grid of points
x, y = np.meshgrid(np.linspace(0, N-1, N), np.linspace(0, N-1, N))
plt.scatter(x, y, color='r', s=1)
'''
# Plots
plt.figure()
plt.xlim(-1,N)
plt.ylim(-1,N)
plt.quiver(U, V, pivot='mid', units='inches', scale=N/4)
plt.show()

fig    = plt.figure()
quiver = plt.quiver(U, V, pivot='mid', units='inches', scale=N/4)

#def init():

def update(frame):#, *args):
    i = np.random.randint(N)
    j = np.random.randint(N)
    U[i,j] *= -1
    plt.quiver(U,V)
    return quiver

# Animate
ani = animation.FuncAnimation(fig, update, frames = N_sweeps, interval = nd, blit = True, repeat = False)

plt.show()
exit()