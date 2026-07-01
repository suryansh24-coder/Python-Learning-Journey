import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Marks":[10,np.nan,30,np.nan,50]
})

print(df)

print(df.interpolate())

print(df.ffill())

print(df.bfill())

print(df.isna().sum())

print(df.notna())