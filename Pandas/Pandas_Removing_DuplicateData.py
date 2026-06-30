import pandas as pd 
x = pd.read_csv('dirtyData.csv')
print(x.to_string())
 
import pandas as pd 
x = pd.read_csv('dirtyData.csv')
print(x.duplicated())
 
import pandas as pd 
x = pd.read_csv('dirtyData.csv')
x.drop_duplicates(inplace=True)
print(x.to_string()) 
 
 
 