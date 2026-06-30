import pandas as pd 
df = pd.read_csv('fitness_data.csv')
print(df.to_string()) 
print(df)

import pandas as pd 
print(pd.options.display.max_rows)
print(pd.options.display.max_columns)

import pandas as pd 
pd.options.display.max_rows = 9999 
df = pd.read_csv('fitness_data.csv')
print(df)

