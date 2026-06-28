import numpy as np 
x = np.array([1,1,1,2,2,2,3,4,5,6,7,8,9,10])
xnew  = np.unique(x)
print(xnew)

y = np.array([1,2,3,4,5])
y1 = np.array([3,4,5,6,7])
ynew = np.union1d(y,y1)
ynew1 = np.intersect1d(y,y1 , assume_unique=True)
ynew2 =np.setdiff1d(y,y1, assume_unique=True)
ynew3 = np.setxor1d(y,y1,assume_unique=True)
print(ynew)
print(ynew1)
print(ynew2)
print(ynew3)





