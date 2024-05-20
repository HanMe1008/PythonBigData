import pandas as pd
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
s3 = pd.concat([s1, s2])
s3 = pd.concat([s1, s2], keys=['s1', 's2'],
               names=['Series name', 'Row ID'])
print(s3)