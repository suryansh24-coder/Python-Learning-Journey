from numpy import random 
 
x = random.zipf(a=2 , size=(2,3)) 
print(x) 

from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns 

sns.kdeplot(random.zipf(a=2 ,size =1000))  
sns.kdeplot(x[x<10])
plt.show()


