import pandas as pd 
x = pd.read_csv('dirtyData.csv')
print(x.to_string())

import pandas as pd 
x = pd.read_csv('dirtyData.csv')
xnew = x.dropna()
print(xnew.to_string())
 
import pandas as pd 
x = pd.read_csv('dirtyData.csv')
x.dropna(inplace=True)
print(x.to_string())

import pandas as pd 
x = pd.read_csv('dirtyData.csv')
x.fillna(230 , inplace=True)
print(x.to_string())

import pandas as pd
x = pd.read_csv('dirtyData.csv')
print(x)
x["calories"].fillna(130 , inplace=True)
print(x.to_string())

import pandas as pd 
x = pd.read_csv('dirtyData.csv')
y = x["calories"].mean()
x["calories"].fillna(y ,inplace=True)
print(x.to_string())

import pandas as pd 
x = pd.read_csv('dirtyData.csv')
y = x["calories"].median()
x["calories"].fillna(y ,inplace=True)
print(x.to_string())

import pandas as pd 
x = pd.read_csv('dirtyData.csv')
y = x["calories"].mode()[0]
x["calories"].fillna(y ,inplace=True)
print(x.to_string())




