import numpy as np 
n = int(input("Enter the size of spilitting :\t"))
x = np.array([1,2,3,4,5,6])
x1 = np.array_split(x,n)
print(x1[0])
print(x1[1])

import numpy as np
c = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
c1 = np.array_split(c,3)
print(c1)

import numpy as np 
v = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]) 
v1 = np.array_split(v , 3 , axis=1)
print(v1)
v2 = np.hsplit(v ,3)
print(v2)











