# Numerical evaluation of a 1-dimensional quantum harmonic oscillator
# Example from: arXiv:hep-lat/0506036
# By Amol Deshmukh, The City College of New York, 2 May 2018.

import numpy as np
from math import exp
from scipy import integrate

N=10        #Integration interval
x_init=0    #Initial position of the particle 
a=1         #Lattice spacing

def f(x_1,x_2,x_3):
	return exp(-(1/2)*(x_1-x_init)**2-(1/2)*(x_2-x_1)**2-(1/2)*(x_3-x_2)**2-(1/2)*(x_init-x_3)**2
		+a*(1/2)*(-x_1**2-x_2**2-x_3**2-2*x_init**2))

a,b=integrate.nquad(f,[[-N,N],[-N,N],[-N,N]])

prop=a*(1/(2*np.pi))**(4/2)
	
print("Numerical value of the propagator is {:f}, with the uncertainty of {:g}".format(prop,b))
