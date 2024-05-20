import pandas as pd
import numpy as np
df2 = pd.DataFrame(np.random.randn(6,4),
                   columns = ["A", "B", "C", "D"],
                   index = pd.date_range("20240510", periods=6))
dates = df2.index
random_dates = np.random.permutation(dates)
df2 = df2.reindex(index=random_dates, columns=["D", "B", "C", "A"])

df2["E"] = np.random.randint(0, 6, size=6)
df2["F"] = ["alpha", "beta", "gamma", "gamma", "alpha", "gamma"]
print(df2)
#df2 = df2["F"].isin(["alpha", "beta"])     # True/False로 확인
df2 = df2.loc[df2["F"].isin(["alpha", "beta"]), :]
print(df2) 