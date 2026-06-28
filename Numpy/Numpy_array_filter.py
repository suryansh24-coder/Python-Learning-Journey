import numpy as np 
x = np.array([40,41,42,43,44])
x1 = [True ,False ,True ,False ,True]
x2 = x[x1]
print(x2)

import numpy as np 
y = np.array([0,1,25,52,4,5,6,2,25,1422])
y1 =[]
for i in y :
    if(i > 5):
        y1.append(True)
    else :
        y1.append(False)
        
y2 = y[y1]

print(y)
print(y1)
print(y2)

import numpy as np 
z = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
z1 = []
for i in z :
    if i % 2 == 0 :
        z1.append(True)
    else :
        z1.append(False)
z2 = z[z1]

print(z)
print(z1)
print(z2)

import numpy as np
v = np.array([41,42,43,44,45,46,47,48,49,50])
v1 = v > 42
v2 = v[v1]
print(v)
print(v1)
print(v2)












