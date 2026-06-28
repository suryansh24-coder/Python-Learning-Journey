import numpy as np 
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b = a.reshape(4,3)
c = a.reshape(2,3,2)
print(b)
print(c)

import numpy as np 
f = np.array([1,2,3,4,5,6,7,8,9,10])
print(f.reshape(2,5).base)

import numpy as np 
n = np.array([1,2,3,4,5,6,7,8])
n1 = n.reshape(2,2,-1)
print(n1) 

import numpy as np 
j = np.array([[1,2,3],[4,5,6]])
j1 = j.reshape(-1)
print(j)
print(j1)





