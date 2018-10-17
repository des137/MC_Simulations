#######################################################################
#!/usr/bin/env python3
"""
--utf--
Author: Amol Deshmukh
10/11/2018
Monte Carlo evaluation of pi in a hypersphere.
"""

import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt
from numpy import random


def pi_calculator(n_points, n_dim):
	"""
	n_points: number of random points for the analysis
	n_dim: number of dimensions of a hypercube
	"""
	x = []
	for _ in range(n_dim): x.append(2*random.rand(n_points)-1)
	radius_squared = 0	
	for i in range(n_dim):
		radius_squared += x[i]**2	
		distance = (radius_squared)**0.5 
	pts_inside = distance[distance < 1]
	pi = (2**n_dim*(len(pts_inside)/float(n_points))*gamma((n_dim/2)+1))**(2/n_dim)	
	return pi

def ensemble_pi_calculator(n_sim, n_points, n_dim):
	"""
	n_sim: number of Monte Carlo simulations
	n_points: number of random points for the analysis
	n_dim: number of dimensions of a hypercube
	"""
	pi_ensemb = []
	for _ in range(n_sim): pi_ensemb.append(pi_calculator(n_points, n_dim))
	return sum(pi_ensemb)/float(len(pi_ensemb))

def main():
	pi_2 = []
	for i in range(7):
		pi_2.append(ensemble_pi_calculator(10**2, 10**i	, 2))
	pi_8 = []
	for i in range(7):
		pi_8.append(ensemble_pi_calculator(10**2, 10**i, 8))
	pi_14 = []
	for i in range(7):
		pi_14.append(ensemble_pi_calculator(10**2, 10**i, 14))
	pi_20 = []
	for i in range(7):
		pi_20.append(ensemble_pi_calculator(10**2, 10**i, 20))		
	plt.plot(pi_2, '--o')
	plt.plot(pi_8, '--o')
	plt.plot(pi_14, '--o')
	plt.plot(pi_20, '--o')
	plt.plot([3.1416, 3.1416, 3.1416, 3.1416, 3.1416, 3.1416, 3.1416], '-')
	plt.xlabel('$Log_{10}(N)$')
	plt.xlim(1,6)
	plt.ylim(0,3.8)
	plt.legend([r'$d$ = 2',r'$d$ = 8',r'$d$ = 14',r'$d$ = 20'])
	plt.grid(True)
	plt.show()

if __name__ == '__main__':
	main()

	#######################################################################
	# Addition 1
	#######################################################################
	x = np.linspace(0.001,30,100)
	plt.plot(x, (1/(2**(2/2)*gamma(2/2)))*x**((2/2)-1)*np.exp(-x/2))
	for k in range(8,21,6):
		plt.plot(x, (1/(2**(k/2)*gamma(k/2)))*x**((k/2)-1)*np.exp(-x/2))

	plt.xlim(0,30)
	plt.ylim(0,.16)
	plt.grid(True)
	plt.legend([r'$d$=2',r'$d$=8',r'$d$=14',r'$d$=20'])
	#plt.show()
	plt.savefig('mama')

	#######################################################################
	# Addition 2
	#######################################################################
	x = np.linspace(1,10,100)
	print(x)

	plt.plot(x,np.pi**(x/2)*(.5)**x/gamma((x/2)+1))
	plt.ylim(0,1.1)
	plt.xlim(1,10)
	plt.grid(True)
	plt.show()
