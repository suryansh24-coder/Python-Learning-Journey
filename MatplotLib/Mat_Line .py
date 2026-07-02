import matplotlib.pyplot as plt 
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints , linestyle='dotted')
plt.plot(ypoints , linestyle='Dashed')
plt.plot(ypoints , linestyle='Dashdot')
plt.plot(ypoints , linestyle='solid')

plt.show()  

import matplotlib.pyplot as plt 
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints , color='r')
plt.plot(ypoints , linewidth=20)
plt.show()

import matplotlib.pyplot as plt 
import numpy as np

xpoints = np.array([3,8,1,10])
ypoints = np.array([6,2,7,11])
plt.plot(xpoints, ypoints, color='r', linewidth='10')
plt.plot(xpoints)
plt.plot(ypoints)
plt.show()

