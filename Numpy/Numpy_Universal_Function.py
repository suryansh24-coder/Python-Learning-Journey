x = [1,2,3,4,5,6]
y = [6,7,8,5,9,1,11]
z = []
for i , j in zip(x,y):
      z.append(i+j) 
print(z)

import numpy as np 
x = [1,2,3,4,5,6]
y = [6,7,8,5,9,1,11]
z = np.add(x,y)
print(z)

