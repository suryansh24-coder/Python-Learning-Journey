# import pandas as pd 
# df = pd.DataFrame({
#                "a" : [4,5,6] ,
#                "b" : [7,8,9] ,
#                "c" : [10,11,12]
#                } , index=[1,2,3])
# print(df)

# import pandas as pd 
# df = pd.DataFrame([[4,5,6],[7,8,9],[10,11,12]] , index=[1,2,3] , columns=['a','b','c'])
# print(df)

import pandas as pd 
df = pd.DataFrame({
               "a" : [4,5,6] ,
               "b" : [7,8,9] ,
               "c" : [10,11,12]
               } , index=pd.MultiIndex.from_tuples([('d',1) , ('d',2),('e',2)], names=['N','V']))
print(df)
 