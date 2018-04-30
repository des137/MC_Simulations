#Law of large numbers
import numpy as np
import matplotlib.pyplot as plt
import random

P=np.zeros(100000)

for i in range(len(P)):
	P[i]=random.random()+random.random()+random.random()+random.random()

print(len(np.arange(len(P))))
print(np.array([[1,0,0],[0,1,2]]).shape)
print(len(P))
plt.hist(P,bins=100)
plt.show()
