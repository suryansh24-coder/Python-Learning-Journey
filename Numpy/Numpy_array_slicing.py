import numpy as np 

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a[1:5])
print(a[1:5:2])
print(a[1:])
print(a[0:])
print(a[ :10])

import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
print(x[-4 : -1])
print(x[ : -1])
print(x[-10 : ])
print(x[-6 : -1 : 2])

import numpy as np 

b = np.array([0,1,2,3,4,5,6,7,8,9,10])
print(b[0:12 : 1])
print(b[1:12:1])
print(b[0:12 : 2])
print(b[1:12:2])
print(b[::2])
print(b[::3])

import numpy as np 
c = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(c[1,1:4])

import numpy as np 
v = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(v[0:2 ,2])
print(v[0:2 , 1:4])


import numpy as np 
h = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print(h[0:3,0:3,1:4])

