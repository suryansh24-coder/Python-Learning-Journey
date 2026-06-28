import numpy as np 
x = np.sin(np.pi/2)
print(x)
x1 = np.array([1,2,3,4,5,6])
x2 = np.array([np.pi/2 , np.pi/3 , np.pi/4 , np.pi/5])
xnew =np.sin(x1)
n = np.sin(x2)
print(xnew)
print(n)

import numpy as np 
x = np.array([90,180,270,360])
xnew = np.deg2rad(x)
print(xnew) 

import numpy as np 
x = np.array([np.pi/2 , np.pi/4 , np.pi , 1.5*np.pi/6])
xnew = np.rad2deg(x)
print(xnew)

y = np.arcsin(1.0)
print(y)

k = np.array([1,-1,0.1,0.5])
knew = np.arcsin(k)
print(knew)

base = int(input("Enter the value of base : "))
perp = int(input("Enter the value of perpendicular : "))
x = np.hypot(base,perp)
print(x)



