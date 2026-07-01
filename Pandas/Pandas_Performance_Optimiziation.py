import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C"],
    "Sales":[100,200,300],
    "Cost":[60,100,150]
})

print(df.query("Sales > 150"))

df.eval("Profit = Sales - Cost", inplace=True)

df["Bonus"] = df["Sales"] * 0.10

print(df.memory_usage())

df["Sales"] = df["Sales"].astype("int16")

print(df.info())
for row in df.itertuples():
    print(row.Name)