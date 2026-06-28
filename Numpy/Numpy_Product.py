import numpy as np 

x = np.array([1,2,3,6,4,5])
x3 = np.array([7,8,9,10,11,12])
x1 = np.prod(x)
x6 = np.prod(x3)
print(x1)
print(x3)
x4 = np.prod([x,x3])
print(x4)
y = np.cumprod(x)
print(y)





