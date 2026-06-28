import numpy as np 
x = np.array([1, 2, 3,4,5,6,7,8,9,10])
print(x)
print(type(x))
 
import numpy as np

y = np.array((1,2,3,4,5,6,7,8,9,10))
print(y)
print(type(y))  

import numpy as np

z = np.array(42)
print(z)

import numpy as np
a = np.array([1,2,3,4,5])
print(a)

import numpy as np
b = np.array([[1,2,3],[4,5,6]])
print(b)

import numpy as np
c = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])

print(c)

import numpy as np

q = np.array(42)
w = np.array([1,2,3,45,6,7,8,9,10])
e = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
r = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
s = np.array([[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]],[[[19,20,21],[22,23,24],[25,26,27]],[[28,29,30],[31,32,33],[34,35,36]]]])

print(q.ndim)
print(w.ndim)
print(e.ndim)     
print(r.ndim)
print(s.ndim)

import numpy as np

g = np.array([1,2,3,4,5],ndmin=5)
print(g)
print("No. of Dimesnions : ",g.ndim)






