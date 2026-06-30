import pandas as pd 
data = {
    "Name" : ["Suryansh" , "Rahul" , "Hariom" ,"Harsh" ,"Ramesh", "Aman"],
    "Age"  : [19,38,20,24,25,40],
    "Country" : ["UK","USA","IND","PAK","AUS","IRE"]
}
df = pd.DataFrame(data)
print(df)
element = df.iloc[1,2]
subset = df.iloc[1:3 , 0:2]
print(element)
print(subset)