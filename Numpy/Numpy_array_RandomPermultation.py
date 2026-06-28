import numpy as np 
from numpy import random 
x = np.array([1,2,3,4,5,6])
random.shuffle(x)
print(x)
x1 = random.permutation(x)
print(x)
print(x1) 



