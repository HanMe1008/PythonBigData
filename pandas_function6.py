from email.utils import decode_rfc2231
import pandas as pd
import numpy as np
df2 = pd.DataFrame(np.random.randn(6,4),
                   columns = ["A", "B", "C", "D"],
                   index = pd.date_range("20240510", periods=6))
dates = df2.index
random_dates = np.random.permutation(dates)
df2 = df2.reindex(index=random_dates, columns=["D", "B", "C", "A"])
print(df2)

# index 기준
df2 = df2.sort_index(axis=0)    # 행 index 오름차순
print(df2)
df2 = df2.sort_index(axis=1 )    # 열 index 오름차순
print(df2)
# 내림차순 하려면 매개변수에 ascending=False 추가

# value 기준
df2 = df2.sort_values(by="D")
print(df2)
df2 = df2.sort_values(by="B", ascending=False)
print(df2)
