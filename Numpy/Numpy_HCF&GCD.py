import numpy as np 
x = 6
y = 9
xy = np.gcd(x,y)
print(xy)

c = np.array([1,2,3,4])
v = np.array([2,4,6,8])
cv = np.gcd.reduce([v,c])
print(cv)
g = np.array([20,8,32,16,36,64])
h = np.gcd.reduce(g)
print(h)