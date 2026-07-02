import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()

import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
myLabels = ["Python", "C++", "Ruby", "Java"]
plt.pie(y, labels=myLabels)
plt.show()

import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
myLabels = ["Python", "C++", "Ruby", "Java"]
plt.pie(y, labels=myLabels , startangle=90)
plt.show()

import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
myLabels = ["Python", "C++", "Ruby", "Java"]
myexplode = [0.2,0,0,0]
    
plt.pie(y, labels=myLabels , startangle=90, explode=myexplode)
plt.show()

import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
myLabels = ["Python", "C++", "Ruby", "Java"]
myexplode = [0.2,0,0,0]
    
plt.pie(y, labels=myLabels , startangle=90, explode=myexplode , shadow=True)
plt.show()

import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
myLabels = ["Python", "C++", "Ruby", "Java"]
mycolors = ["m", "hotpink", "b", "c"]
    
plt.pie(y, labels=myLabels , startangle=90, colors=mycolors, shadow=True)
plt.show()


import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
myLabels = ["Python", "C++", "Ruby", "Java"]
mycolors = ["m", "hotpink", "b", "c"]
    
plt.pie(y, labels=myLabels , startangle=90, colors=mycolors, shadow=True)
plt.legend(title="Programming Languages")
plt.show()

