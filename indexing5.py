import numpy as np 
import pandas as pd
data = {"names": ["KIM", "KIM", "KIM", "LEE", "LEE"],
        "score": [99.5, 95.5, 90.5, 94.5, 85.5],
        "year": [2018, 2019, 2020, 2021, 2022]}
df = pd.DataFrame(data)
df = pd.DataFrame(data, columns=["year", "names", "score", "penalty"],
                         index=["one", "two", "three", "four", "five"])
df["penalty"]=[0.1, 0.2, 0.3, 0.4, 0.5]

val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four", "five"])
df["debt"] = val

df.index.name = "Order"
df.columns.name = "Info"
df.loc["six", : ] = [2023, "PARK", 94.0, 0.6, 2.0]

# 1
#df = df["year"] > 2018
#print(df)

# 2
#df = df.loc[df["year"] > 2018, :]
#print(df)

# 3
#df = df.loc[df["names"]=="KIM", ["names", "score"]]
#print(df)

# 4
#df = df.loc[(df["score"] > 90.0) & (df['score'] < 99.0), : ]
#print(df)

# 5
df.loc[(df["score"] > 90.0), "penalty"] = 0
print(df)