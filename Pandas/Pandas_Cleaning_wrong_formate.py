import pandas as pd
x = pd.read_csv('dirtyData.csv')
print(x.to_string())

import pandas as pd
x = pd.read_csv('dirtyData.csv')
x['date'] = pd.to_datetime(x['date'])
print(x.to_string())

import pandas as pd 
x = pd.read_csv('dirtyData.csv')
x['date'] = pd.to_datetime(x['date'])
x.dropna(subset=['date'] ,inplace=True)
print(x.to_string())













