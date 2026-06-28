import numpy as np 
x = np.array([1,2,3,4,5,6,5,4,4,4])
x1 = np.where(x==4)
print(x1)

x3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x4 = np.where(x3 % 2 == 0)
print(x4)
x5 = np.where(x3 % 2 != 0)
print(x5)

x6 = np.array([6,7,8,9])
x0 = np.searchsorted(x6 , 7 , side='right')
x7 = np.searchsorted(x6 , 7 , side='left')
print(x0,x7)
x8 = np.searchsorted(x6 , [2,4,5])
print(x8)
































