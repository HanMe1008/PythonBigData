import numpy as np 
import pandas as pd
data = {"names": ["KIM", "KIM", "KIM", "LEE", "LEE"],
        "score": [99.5, 95.5, 90.5, 94.5, 85.5],
        "year": [2018, 2019, 2020, 2021, 2022]}
df = pd.DataFrame(data)
df2 = pd.DataFrame(data, columns=["year", "names", "score", "penalty"],
                         index=["one", "two", "three", "four", "five"])

print(df2)
print(df2.describe())