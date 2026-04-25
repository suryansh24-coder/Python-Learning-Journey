import numpy as np 
print(np.__version__)
a = np.array([1,2,3])  
print(a)
b = np.array([9.0,5.0,6.0],[6.0,4.0,7.0])
print(b) 
# Get Diension
a.ndim
print(a.ndim)
# Get Shape
a.shape
print(a.shape)
# Get Type 
print(a.dtype)
# Get size
print(a.itemsize)
# Get total size
print(a.nbytes)