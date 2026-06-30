import pandas as pd 
x = pd.read_csv('dirtyData.csv')
print(x.to_string())

import pandas as pd 
x = pd.read_csv('dirtyData.csv')
x.loc[133 , 'calories'] = 150
print(x.to_string())

import pandas as pd 
x = pd.read_csv('dirtyData.csv')
for i in x.index :
    if x.loc[i , "calories"]  > 120 :
        x.loc[i ,"calories"] = 120 
        
print(x.to_string())        
    
import pandas as pd 
x = pd.read_csv('dirtyData.csv')
for i in x.index :
    if x.loc[i , "calories"]  < 200 :
        x.dropna(i , inplace =True)
        
print(x.to_string())        
 

