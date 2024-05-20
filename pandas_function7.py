# 정렬함수
import pandas as pd
import numpy as np
df2 = pd.DataFrame(np.random.randn(6,4),
                   columns = ["A", "B", "C", "D"],
                   index = pd.date_range("20240510", periods=6))
dates = df2.index
random_dates = np.random.permutation(dates)
df2 = df2.reindex(index=random_dates, columns=["D", "B", "C", "A"])
print(df2)

df2["E"] = np.random.randint(0, 6, size=6)
df2["F"] = ["alpha", "beta", "gamma", "gamma", "alpha", "gamma"]
df2 = df2.sort_values(by=["E", "F"])
print(df2)

# 기타함수
# 중복 제거 매소드 : unique()
df3 = df2["F"].unique()
print(df3)

# 동일 값 몇 개인지 매소드 : value_counts()
df3 = df2["F"].value_counts()
print(df3)