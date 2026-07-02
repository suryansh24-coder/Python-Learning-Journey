import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x, y)
plt.xlabel("Average Oxygen")
plt.ylabel("Our Calories")
plt.title(" Oxygen vs. Calories")    
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'red','size':15}

plt.plot(x, y)
plt.xlabel("Average Oxygen", fontdict=font2)
plt.ylabel("Our Calories", fontdict=font2)
plt.title("Health Monitoring", fontdict=font1)    
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'red','size':15}

plt.plot(x, y)
plt.xlabel("Average Oxygen", fontdict=font2 , loc='left')
plt.ylabel("Our Calories", fontdict=font2, loc='top')
plt.title("Health Monitoring", fontdict=font1 , loc='right')    
plt.show()




