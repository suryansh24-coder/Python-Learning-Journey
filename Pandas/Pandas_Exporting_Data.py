import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C"],
    "Age":[20,21,22],
    "Salary":[50000,60000,70000]
})

df.to_csv("employees.csv", index=False)

df.to_excel("employees.xlsx", index=False)

df.to_json("employees.json")
print(df.to_dict())

print(df.to_numpy())

df.to_pickle("employees.pkl")

df.to_html("employees.html")

print(df.to_markdown())