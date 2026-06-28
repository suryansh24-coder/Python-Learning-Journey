import numpy as np 
x = np.array([1,2,3,4,5])
x1 = np.array([6,7,8,9,10])
x2 = np.add(x,x1)
print(x2)

x3 = np.sum([x,x1])
x4 = np.sum([x,x1] , axis=1)
x5 = np.cumsum(x)
print(x3)
print(x4)
print(x , "\n" , x5)








