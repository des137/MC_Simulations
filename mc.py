# -------Monte Carlo evaluation of pi-------
# By Amol Deshmukh, The City College of New York, 16 April 2018.
import numpy as np 
import random

N=100000
a=np.random.rand(N)
b=np.random.rand(N)
c=(a**2+b**2)**(1/2)

for i in range(len(c)):
	if c[i]>1:
		c[i]=0
	else:
		c[i]=1	

d=np.sum(c)
pi=(d/N)*4
print(pi)
