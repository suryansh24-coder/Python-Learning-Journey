import numpy as np 
a = np.array([1,2,3,4,6,5,8,7,9,10])
print(a.dtype)
b = np.array({"apple","mango","banana"})
print(b.dtype)
c = np.array(["apple","mango","banana"])
print(c.dtype)
d = np.array((1,2,3,4,5,6,78))
print(d.dtype)

import numpy as np 
a = np.array([1,2,3,4,5,6,7,8,9,10], dtype='S')
print(a)
print(a.dtype)

import numpy as np 
a = np.array(['a','2','3'] , dtype ='i')
print(a.dtype) #This will produce an array !

import numpy as np 

k = np.array([1.1,1.2,1.3,1.4,1.5,1.6])
k1 = k.astype('i')
print(k.dtype)
print(k1.dtype)
print(k1)
print(k)

import numpy as np 
o = np.array([1,2,3,4,5,6,7,8,9,10])
o1 = o.astype(bool)
print(o1.dtype)
print(o1)


















