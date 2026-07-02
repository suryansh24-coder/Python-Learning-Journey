import matplotlib.pyplot as plt
import numpy as np
 
ypoints = np.array([3,8,1,10]) 
plt.plot(ypoints , marker='*')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
 
ypoints = np.array([3,8,1,10]) 
plt.plot(ypoints , marker='o')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints ,'o:r')
plt.plot(ypoints ,'o-.c')
plt.plot(ypoints ,'o-')
plt.show()
 
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10]) 
plt.plot(ypoints , marker='o', markersize=20)   
plt.show()
 
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints , marker='o', markersize=20, markeredgecolor='r')
plt.show()

 
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints , marker='o', markersize=20, markerfacecolor='c')
plt.show()
 
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints , marker='o',ms=20 , mec='k' , mfc='c') 
plt.show()
 