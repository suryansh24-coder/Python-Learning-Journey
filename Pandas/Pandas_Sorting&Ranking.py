import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C","D","E"],
    "Age":[22,30,19,28,25],
    "Salary":[50000,80000,45000,70000,60000]
})

print(df.sort_values("Salary"))

print(df.sort_values("Salary", ascending=False))

print(df.sort_values(["Age","Salary"]))

print(df.sort_index())

print(df.nlargest(3,"Salary"))

print(df.nsmallest(2,"Salary"))

df["Rank"] = df["Salary"].rank(ascending=False)

print(df)