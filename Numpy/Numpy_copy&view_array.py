import numpy as np 
a = np.array([1,2,3,4,5,6,7,8,9,10])
a1 = a.copy()
print(a1)
print(a)

import numpy as np 
b = np.array([1,2,3,4,5,6,7,8,9,10])
b1 = b.copy()
b2 = b.view()
print(b2)
print(b1)
print(b)

b[0] = 42 
print(b)
print(b1)