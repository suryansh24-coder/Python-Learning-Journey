import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 

df1 = sns.load_dataset('iris')
sam = df1.head()

corr = df1.corr(numeric_only=True)
sns.heatmap(
    corr , 
    annot=True
) 
plt.show()
