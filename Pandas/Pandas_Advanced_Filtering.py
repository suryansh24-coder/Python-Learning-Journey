import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 25, 18, 30, 22],
    "Salary": [40000, 60000, 45000, 70000, 55000],
    "Department": ["IT", "HR", "Sales", "IT", "HR"]
})

print(df[df["Age"] > 20])

print(df[(df["Age"] > 20) & (df["Salary"] > 50000)])

print(df[df["Department"].isin(["IT", "HR"])])

print(df[df["Salary"].between(45000, 65000)])

print(df.query("Age > 20 and Salary > 50000"))

print(df.filter(items=["Name", "Salary"]))

print(df.where(df["Salary"] > 50000))

print(df.mask(df["Salary"] > 50000))

print(df.loc[df["Department"] == "IT"])

print(df.iloc[0:3])