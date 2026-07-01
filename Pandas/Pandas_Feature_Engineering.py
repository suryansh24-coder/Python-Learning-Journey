import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["alice", "bob", "charlie", "david", "eva"],
    "Age": [18, 25, 35, 42, 28],
    "Sales": [5000, 7000, 9000, 8000, 6500],
    "Cost": [3000, 4000, 5000, 4500, 3500],
    "Department": ["IT", "HR", "IT", "Sales", "HR"],
    "Date": ["2024-01-10", "2024-02-15", "2024-03-20", "2024-04-05", "2024-05-25"]
})

df["Profit"] = df["Sales"] - df["Cost"]
df["Profit_Percentage"] = (df["Profit"] / df["Sales"]) * 100
df["Total"] = df["Sales"] + df["Cost"]

df.insert(1, "Employee_ID", [101, 102, 103, 104, 105])

df = df.assign(
    Bonus=df["Sales"] * 0.10,
    Tax=df["Sales"] * 0.05
)

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Weekday"] = df["Date"].dt.day_name()
df["Quarter"] = df["Date"].dt.quarter
df["Month_Name"] = df["Date"].dt.month_name()
df["Is_Month_Start"] = df["Date"].dt.is_month_start
df["Is_Month_End"] = df["Date"].dt.is_month_end

df["Upper"] = df["Name"].str.upper()
df["Lower"] = df["Name"].str.lower()
df["Title"] = df["Name"].str.title()
df["Length"] = df["Name"].str.len()
df["First_Char"] = df["Name"].str[0]
df["Last_Char"] = df["Name"].str[-1]
df["Contains_A"] = df["Name"].str.contains("a")
df["Starts_With_A"] = df["Name"].str.startswith("a")
df["Ends_With_E"] = df["Name"].str.endswith("e")
df["Replace_A"] = df["Name"].str.replace("a", "@")
df["Split"] = df["Name"].str.split("a")

df["Status"] = np.where(df["Profit"] > 3000, "High", "Low")

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 20, 30, 40, 100],
    labels=["Teen", "Young", "Adult", "Senior"]
)

df["Sales_Quartile"] = pd.qcut(
    df["Sales"],
    q=4,
    labels=["Q1", "Q2", "Q3", "Q4"]
)

encoded = pd.get_dummies(df, columns=["Department"])

df["Age"] = df["Age"].astype("float")
df["Sales"] = pd.to_numeric(df["Sales"])

df["Profit"] = df["Profit"].fillna(0)

print(df)
print(encoded)