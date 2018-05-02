import numpy as np
from math import exp
from scipy import integrate

N=3.5
i=0

def f(x_1,x_2,x_3,x_4):
	return exp(-(x_1-i)**2-(x_2-x_1)**2-(x_3-x_2)**2-(x_4-x_3)**2-(i-x_4)**2
		+(1/4)*(-x_1**2-x_2**2-x_3**2-x_4**2-2*i**2))

a,b=integrate.nquad(f,[[-N,N],[-N,N],[-N,N],[-N,N]])

c=a*(1/np.pi)**(6/2)
	
print("Result is {:f} and {:g}".format(c,b))
