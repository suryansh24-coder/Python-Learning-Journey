import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([80,85,90,95,100,105,110])
ypoints = np.array([240,250,260,270,280,290,300])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'red','size':15}

plt.plot(xpoints, ypoints)
plt.title("Health Monitoring", fontdict=font1)
plt.xlabel("Average Oxygen", fontdict=font2)   
plt.ylabel("Our Calories", fontdict=font2)
plt.grid(axis='x') 
plt.show() 

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([80,85,90,95,100,105,110])
ypoints = np.array([240,250,260,270,280,290,300])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'red','size':15}

plt.plot(xpoints, ypoints)
plt.title("Health Monitoring", fontdict=font1)
plt.xlabel("Average Oxygen", fontdict=font2)   
plt.ylabel("Our Calories", fontdict=font2)
plt.grid(axis='y')
plt.show() 

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([80,85,90,95,100,105,110])
ypoints = np.array([240,250,260,270,280,290,300])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'red','size':15}

plt.plot(xpoints, ypoints)
plt.title("Health Monitoring", fontdict=font1)
plt.xlabel("Average Oxygen", fontdict=font2)   
plt.ylabel("Our Calories", fontdict=font2)
plt.grid(axis='both')
plt.show() 


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([80,85,90,95,100,105,110])
ypoints = np.array([240,250,260,270,280,290,300])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'red','size':15}

plt.plot(xpoints, ypoints)
plt.title("Health Monitoring", fontdict=font1)
plt.xlabel("Average Oxygen", fontdict=font2)   
plt.ylabel("Our Calories", fontdict=font2)
plt.grid(axis='both', color ="cyan" , linestyle="--" , linewidth=0.5)

plt.show() 










