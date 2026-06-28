from numpy import random 
x = random.poisson(lam=2 , size=10)
print(x) 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 
sns.displot(random.poisson(lam=2 , size=10))
plt.show()

from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns 

sns.dispolt(random.poisson(lam=2 ,size=10), label='Poisson')
sns.displot(random.normal(loc = 2 , scale = 1 , size=10), label='Normal')
plt.show()












