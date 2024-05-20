import pandas as pd
s1 = pd.Series(['a', 'b'])
print(s1)
s2 = pd.Series(['c', 'd'])
print(s2)
#s3 = pd.concat([s1, s2])
s3 = pd.concat([s1, s2], ignore_index=True) # 기존 색인을 지우고 결과에서 재설정
print(s3)