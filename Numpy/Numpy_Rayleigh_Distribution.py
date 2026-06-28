from numpy import random 
x = random.rayleigh(scale=2, size=(2,3))
print(x)

from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns 

sns.kdeplot(random.rayleigh(size=(1000)))
plt.show()





