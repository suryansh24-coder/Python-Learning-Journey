import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 

df1 = sns.load_dataset('iris')
sam = df1.head()

sns.histplot(
    data = df1 ,
    x = 'Total_bills'
) 
plt.show()
