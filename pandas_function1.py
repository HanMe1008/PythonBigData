import pandas as pd
import numpy as np
data = [[1.4, np.nan],
        [7.1, -4.5],
        [np.nan, np.nan],
        [0.75, -1.3]]
df = pd.DataFrame(data, columns = ["one", "two"],
                        index = ["a", "b", "c", "d"])
print(df)

#df = df.sum(axis=0)    # 열의 합
df = df.sum(axis=1)     # 행의 합
# 둘 다 실행하면 에러
print(df)
