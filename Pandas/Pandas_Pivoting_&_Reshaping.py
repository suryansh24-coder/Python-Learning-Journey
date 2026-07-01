import pandas as pd 

df = pd.DataFrame({
    "Students": ["Alice", "Bob", "Charlie", "David"] ,
    "Subjects": ["Math", "Science", "Math", "Science"],
    "Scores": [85, 90, 78, 88]      
})
print("Original DataFrame:")
print(df)

pivot_df = df.pivot(index="Students", columns="Subjects", values="Scores")
print(pivot_df)

pivot_table_df = df.pivot_table(
    index="Students",
    columns="Subjects",
    values="Scores",
    aggfunc="mean"
)
print(pivot_table_df) 

melt_df = pd.melt(
    pivot_df.reset_index(),
    id_vars="Student",
    var_name="Subject",
    value_name="Marks"
)
print(melt_df)

print(pivot_df.stack())
print(pivot_df.stack().unstack())
print(pd.crosstab(df["Student"], df["Subject"]))