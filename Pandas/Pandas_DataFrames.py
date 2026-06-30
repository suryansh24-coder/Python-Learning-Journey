import pandas as pd 
data = { 
        "cal" : [420,380,390] ,
        "Dur" : [50,40,45]
        }
x = pd.DataFrame(data)
print(x)
print(x.loc[0])
print(x.loc[[0 , 1]])

import pandas as pd 
data = { 
        "cal" : [420,380,390] ,
        "Dur" : [50,40,45]
        }
x = pd.DataFrame(data ,index=["Day 1" , "Day 2" ,"Day 3"])
print(x)

import pandas as pd 
data = { 
        "cal" : [420,380,390] ,
        "Dur" : [50,40,45]
        }
x = pd.DataFrame(data ,index=["Day 1" , "Day 2" ,"Day 3"])
print(x.loc["Day 1"])
print(x.loc[["Day 1" ,"Day 2"]])

import pandas as pd 
fileload = pd.read_csv("Data.csv/or path")
print(fileload)
