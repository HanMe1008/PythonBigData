import numpy as np 
import pandas as pd
data = {"names": ["KIM", "KIM", "KIM", "LEE", "LEE"],
        "score": [99.5, 95.5, 90.5, 94.5, 85.5],
        "year": [2018, 2019, 2020, 2021, 2022]}
df = pd.DataFrame(data)
df = pd.DataFrame(data, columns=["year", "names", "score", "penalty"],
                         index=["one", "two", "three", "four", "five"])
df["penalty"]=[0.1, 0.2, 0.3, 0.4, 0.5]
df["zeros"]=np.arange(5)
val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four", "five"])
df["debt"] = val

df["net_score"] = df["score"] - df["penalty"]
df["high_score"] = df["net_score"] > 90.0

df.index.name = "Order"
df.columns.name = "Info"

del df["zeros"]

print(df.columns)
print(df)