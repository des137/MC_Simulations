# Simulates Ising model using Monte Carlo techniques
# By Amol Deshmukh, The City College of New York, May 2018

import numpy as np
import matplotlib.pyplot as plt

# To create an animation of the Ising model:
import matplotlib.animation as animation

# System parameters
N     = 20		          # Number of lattice sites
N_sim = 3*10**5           # Simulation steps
temp  = 2.3				  # Temperature

#temp  = 0.05*np.array(15) # Temperature values(0.25:3.5)

# Local energy change of the system after a spin flip
def diff_energy(state,i,j):
	return 2*state[i,j]*(state[(i-1)%N,j]+state[i,(j-1)%N]+state[(i+1)%N,j]+state[i,(j+1)%N]) 	
	
def update(state):
	for k in range(N_sim):		
		i = np.random.randint(N)
		j = np.random.randint(N)
		delta_E=diff_energy(state,i,j)
		if delta_E<0 or np.exp(-delta_E/temp)>np.random.uniform(0,1):
			state[i,j] = (-1)*state[i,j]
		magnetization[k] = state.sum()	
			
# Intial state
state = 2*np.random.randint(2, size=(N,N))-1

# Magnetization value holder
magnetization=np.zeros(N_sim)

# Monte Carlo updates
update(state)

# Snapshot of the configuration at the end of Monte Carlo simulation
plt.imshow(state)#, interpolation='nearest')
plt.title('Final configuration of the Ising model')
plt.gray()
plt.show()

# Net Magnetization as a functions of no. of Monte Carlo sweeps
plt.plot(magnetization)
plt.xlabel('No. of sweeps')
plt.ylabel('Net Magnetization')
plt.ylim(-1.1*N**2,1.1*N**2)
plt.grid(True)
plt.show()

# Histogram for 'Net Magnetization'
plt.hist(magnetization,bins=100)
plt.xlim(-1.1*N**2,1.1*N**2)
plt.xlabel('Net Magnetization')
plt.ylabel('Counts')
plt.show()

exit()
#animation.FuncAnimation()
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
#    time_text.set_text(time_template % (i*dt))
    return line#, time_text

img=plt.imshow()

ani = animation.FuncAnimation(img, animate, np.arange(1, len(y)),
                              interval=25, blit=True, init_func=init)