import pandas as pd
import numpy as np
data = [[1.4, np.nan],
        [7.1, -4.5],
        [np.nan, np.nan],
        [0.75, -1.3]]
df = pd.DataFrame(data, columns = ["one", "two"],
                        index = ["a", "b", "c", "d"])
print(df)

# 평균을 계산할 때 NaN이 하나라도 포함되어 있으면 평균=NaN
# skipna=False : NaN 값 포함
# skipna=True  : NaN 값 제외

# 행 평균한 뒤 열 평균 구하기(그러지 않으려면 변수 이름 다르게 지정하기)
df = df.mean(axis=1, skipna=False)  
df = df.mean(axis=0, skipna=True)       
print("Mean of Columns")
print(df)