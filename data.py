import numpy as np
import pandas as pd

df = pd.read_csv("./archive/images_with_countries.csv")
df["date_taken"] = pd.to_datetime(df["date_taken"], format=f"%Y-%m-%d")
filtered = df[df["date_taken"] > "2021-01-01"]

print(len(filtered))
