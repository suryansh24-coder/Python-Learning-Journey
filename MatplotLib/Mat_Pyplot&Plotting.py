# Plotting Line Graphs using Matplotlib :-
import matplotlib.pyplot as plt
import numpy as np 

xpoints = np.array([1,8])
ypoints = np.array([3,10])
plt.plot(xpoints, ypoints)
plt.plot(ypoints, xpoints)
plt.show()

# Plotting without lines : 
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])
plt.plot(xpoints, ypoints, 'o')
plt.plot(ypoints, xpoints, 'o')
plt.show()

# Zig Zag Graph :
import matplotlib.pyplot as plt 
import numpy as np 
xpoints = np.array([1,2,3,4,5,6,7])
ypoints = np.array([3,8,1,10,5,7,9])
plt.plot(xpoints, ypoints)      
plt.show()

# Default X - points :-
import matplotlib.pyplot as plt 
import numpy as np
ypoints = np.array([3,8,1,10,5,7]) 
plt.plot(ypoints)
plt.show()


