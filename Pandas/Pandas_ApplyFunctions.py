import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C"],
    "Salary":[50000,60000,70000],
    "Gender":["M","F","M"]
})

df["Bonus"] = df["Salary"].apply(lambda x: x*0.10)

df["Gender"] = df["Gender"].map({
    "M":"Male",
    "F":"Female"
})
df["Gender"] = df["Gender"].replace("Male","M")

df["Average Salary"] = df.groupby("Gender")["Salary"].transform("mean")

df[["Salary","Bonus"]] = df[["Salary","Bonus"]].applymap(lambda x:int(x))

print(df)