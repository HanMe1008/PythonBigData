import pandas as pd
import numpy as np
data = [[1.4, np.nan],
        [7.1, -4.5],
        [np.nan, np.nan],
        [0.75, -1.3]]
df = pd.DataFrame(data, columns = ["one", "two"],
                        index = ["a", "b", "c", "d"])
print(df)

df = df["one"].sum()            # 특정 열의 합
#df = df.loc["d"].sum()          # 특정 행의 합
# 둘 다 실행하면 에러
print(df)
