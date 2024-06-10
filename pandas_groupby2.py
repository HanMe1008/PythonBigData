import pandas as pd
import numpy as np
ipl_data = {'Team'  : ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'Kings',
                       'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank'  : [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            'Year'  : [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
            'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)
print(df)

# 한 개 이상의 Column을 묶음
df1 = df.groupby(["Team", "Rank"]).sum()
print(df1)

df2 = df.groupby(["Team", "Year"])["Points"].sum()
print(df2)

df3 = df.groupby(["Team", "Rank", "Year"])["Points"].sum()
print(df3)
