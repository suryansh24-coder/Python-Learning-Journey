import pandas as pd

df = pd.DataFrame({
    "Department": ["IT","IT","HR","HR","Sales"],
    "Salary": [50000,60000,45000,47000,55000]
}) 
df.groupby("Department")["Salary"].sum() 
df.groupby("Department")["Salary"].mean() 
df.groupby("Department")["Salary"].mean()
df.groupby("Department")["Salary"].min()
print(df.to_string())

df.groupby("Department")["Salary"].mean()

df.groupby("Department")["Salary"].max()

df.groupby("Department")["Salary"].min()
df.groupby("Department")["Salary"].agg(["mean","max","min"])
print(df.groupby("Department")["Salary"].agg(["mean","max","min"]))


