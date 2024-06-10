import pandas as pd
import numpy as np
ipl_data = {'Team'  : ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'Kings',
                       'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank'  : [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            'Year'  : [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
            'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby("Team")

# 개별 data(전체 data)의 변환을 지원함
score = lambda x: (x)
df = grouped.transform(score)
print(df)

score = lambda x: (x.max())
df = grouped.transform(score)
print(df)

score = lambda x: (x-x.mean())/x.std()
df = grouped.transform(score)
print(df)