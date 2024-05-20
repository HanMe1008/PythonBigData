# 상관계수, 공분산 계산
import pandas as pd
import numpy as np

# np.random.randn : 표준 정규 분포 추출 함수(평균=0, 표준편차=1)
df2 = pd.DataFrame(np.random.randn(6,4),
                   columns = ["A", "B", "C", "D"],
                   index = pd.date_range("20240510", periods=6))
print(df2)

# A열과 B열의 상관계수(corr 함수)
df3 = df2["A"].corr(df2["B"])
print(df3)

# B열과 C열의 공분산(cov 함수)
df4 = df2["B"].cov(df2["C"])
print(df4)

# 모든 열들간의 상관계수
df5 = df2.corr()
print(df5)

# 모든 열들간의 공분산
df6 = df2.cov()
print(df6)