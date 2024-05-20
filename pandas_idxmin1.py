import pandas as pd
import numpy as np
data = [[1.4, np.nan],
        [7.1, -4.5],
        [np.nan, np.nan],
        [0.75, -1.3]]
df = pd.DataFrame(data, columns = ["one", "two"],
                        index = ["a", "b", "c", "d"])
print(df)

# 'one'열에서 최소값을 가진 행의 index
#df = df['one'].idxmin()
# 각 열에서 최소값을 가진 행의 index
#df = df.idxmin()
# 각 행에서 최소값을 가진 열의 index
#df = df.idxmin(axis=1)
# skipna=False : NaN 값을 포함 --> NaN가 포함되면 모두 NaN
df = df.idxmin(axis=1, skipna=False)

print(df)