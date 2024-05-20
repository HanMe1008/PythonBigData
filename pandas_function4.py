# NaN을 대체하는 함수 fillna()
import pandas as pd
import numpy as np
data = [[1.4, np.nan],
        [7.1, -4.5],
        [np.nan, np.nan],
        [0.75, -1.3]]
df = pd.DataFrame(data, columns = ["one", "two"],
                        index = ["a", "b", "c", "d"])
print(df)

one_mean = df.mean(axis=0) ["one"]
two_mean = df.min(axis=0) ["two"]

df["one"] = df["one"].fillna(value=one_mean)
df["two"] = df["two"].fillna(value=two_mean)

print(df)