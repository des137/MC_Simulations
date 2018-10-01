# -------Monte Carlo evaluation of pi in a hypersphere-------
# By Amol Deshmukh, The City College of New York, 01 October 2018.

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

def ensemble(n_sim, n_points, n_dim):
	"""
	n_sim: number of Monte Carlo simulations
	n_points: number of random points for the analysis
	n_dim: number of dimensions of a hypercube
	"""
	pi_ensemb = []

	for _ in range(n_sim): pi_ensemb.append(pi_calculator(n_points, n_dim))

	return sum(pi_ensemb)/float(len(pi_ensemb))

print('Pi using two-dimensional sphere (i.e. circle): {}'.format(ensemble(10**3, 10**6, 2)))

print('Pi using 10-dimensional sphere: {}'.format(ensemble(10**3, 10**6, 10)))
