import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y= np.array([3, 7, 5, 9])
plt.bar(x, y)

for i, value in enumerate(y):
    plt.text(i, value - 3, str(value), ha='center', va='bottom')
plt.show()


import matplotlib.pyplot as plt
import numpy as np 

x = np.array(['A', 'B', 'C', 'D'])
y= np.array([3, 7, 5, 9])
plt.plot(x, y ,"o:c")

for i,j in zip(x,y):
    plt.text(i, j - 0.5, str(j), ha='center', va='bottom')
    
plt.show()




