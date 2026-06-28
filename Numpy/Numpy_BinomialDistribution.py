# from numpy import random 
# x = random.binomial(n=10 , p = 0.5 , size=10)
# print(x)


from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n=10 , p=0.5 , size = 1000) ,label='Normal')
sns.displot(random.binomial(n=10 , p=0.5 , size = 1000) ,label='Binomial')
plt.show()




