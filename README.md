# Monte Carlo Simulations

This repository contains algorithms based on the concept of 'Markov Chain Monte Carlo' for the extraction of thermal eqilibrium properties of statistical systems. It contains codes for Monte Carlo simulations of well known statistical systems known as **'Ising model'** and **'XY model'**. Metropolis algorithm is applied for generating the the equilibrium configurations of these systems distributed according to Boltzmann distribution. The image below shows an example of a  configuration of the Ising Model on a lattice of size 256x256, obtained after approximately a million Markov chain Monte Carlo steps.

<p align="center">
  <img src="https://github.com/des137/mcmc/blob/master/Intermediate_state.png" width="256" title="Ising Model">
</p>

1. [ising.py](https://github.com/des137/Monte_Carlo_Simulations/blob/master/ising/ising.py) implements the metropolis algorithm on the Ising model.
2. [animation.py](https://github.com/des137/Monte_Carlo_Simulations/blob/master/ising/animation.py) creates an animation of the Markov chain of the Ising model configurations.
3. [ising.ipynb](https://github.com/des137/Monte_Carlo_Simulations/blob/master/ising/ising.ipynb) is a jupyter notebook for better visualizations of the thermodynamic variables plotted as functions of Monte Carlo steps.
3. [xy.py](https://github.com/des137/Monte_Carlo_Simulations/blob/master/xy/xy.py) implements the metropolis algorithm on the XY model.
