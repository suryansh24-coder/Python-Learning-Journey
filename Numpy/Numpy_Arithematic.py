import numpy as np
x = np.array([10,11,12,13,14,15])
x1 = np.array([20,21,22,23,24,25])
x2 = np.add(x,x1)
print(x2)

x3 = np.subtract(x1,x)
print(x3)

x4 = np.multiply(x,x1)
x5 = np.divide(x ,x1)
print(x4  , "\n" , x5)



y = np.array([2,3,4,5,6,7,8,9,10])
y1 = np.array([2,2,2,2,2,2,2,2,2])
yy = np.power(y,y1)
print(yy)
y2 = np.remainder(y,y1)
y4 = np.mod(y,y1)
y5 = np.divmod(y,y1)
print(y2 ,"\n" ,y4 , "\n" ,y5) 

c = np.array([-1,-2,-3,-4,-5])
c1 = np.absolute(c)
c2 = np.abs(c)
print(c1 , "\n" , c2)

