import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns

sns.kdeplot(random.normal(size=1000, loc=1, scale=2), label="Normal")
sns.kdeplot(random.binomial(size=1000, n=1, p=0.5), label="Binomial")
sns.kdeplot(random.poisson(size=1000, lam=1), label="Poisson")
sns.kdeplot(random.uniform(size=1000, low=0, high=1), label="Uniform")
sns.kdeplot(random.logistic(size=1000, loc=1, scale=2), label="Logistic")
sns.kdeplot(random.multinomial(size=1000, n=10, pvals=[0.3, 0.7]),label="Multinomial")
sns.kdeplot(random.exponential(size=1000, scale=2), label="Exponential")

plt.legend()
plt.show()
