from numpy import random 
x = random.pareto(size=(2,3),a=2)
print(x)

from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns 

sns.kdeplot(random.pareto(a=2 , size=1000))
plt.show()





