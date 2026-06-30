import pandas as pd 
x = [1,2,3,7,8,9,10]
xnew = pd.Series(x)
print(xnew)
print(xnew[0])

import pandas as pd
x = [1,2,3,4,5]
xnew = pd.Series(x , index=["x","y","z","f","g"])
print(xnew)
print(xnew["x"])

import pandas as pd
cal = {
    "Day 1" : 420 ,
    "Day 2" : 380 ,
    "Day 3" : 390
}
xnew = pd.Series(cal)
print(xnew)
result = pd.Series( cal , index=["Day 1" ,"Day 3"])
print(result)

import pandas as pd
x = {"Cal" : [420,380,390] , "Duration":[50,40,45]}
xnew = pd.DataFrame(x)
print(xnew)

import pandas as pd 
x = {
    "Name" : ["Suryansh", "Rahul" , "Simran", "Ramesh"] , 
    "DOB" : [2006,2007,2008,2009], 
    "College" : ["JSS","JSS","JSS","JSS"], 
    "Salary(LPA)" : [10,15,35,9]
    }
xnew = pd.DataFrame(x)
print(xnew)

