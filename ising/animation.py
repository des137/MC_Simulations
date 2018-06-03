import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm

Nx = 100
Ny = 100
Nf = 10000 #Number of frames
nd = 10 #Delay between frames in miliseconds

state = 2 * np.random.randint(2, size = (Nx, Ny)) - 1

fig = plt.figure(frameon = False)

im = plt.imshow(state, extent=(0, Nx, 0, Ny), interpolation = 'none', animated = True, cmap = cm.binary)

plt.xlabel('x')
plt.ylabel('y')

def update(frame, *args):
	i = np.random.randint(Nx)
	j = np.random.randint(Ny)
	state[i, j] *= -1
	im.set_data(state)
	return im,

ani = animation.FuncAnimation(fig, update, frames = Nf, interval = nd, blit = True, repeat = False)

plt.show()
