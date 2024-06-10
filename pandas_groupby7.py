import pandas as pd
import numpy as np
ipl_data = {'Team'  : ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'Kings',
                       'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank'  : [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            'Year'  : [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
            'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby("Team")

# aggregation (합계) - sum
df = grouped.agg(sum)
print(df)

# aggregation (집계) - np.mean
df = grouped.agg(np.mean)
print(df)

df = grouped.agg([np.sum, np.mean, np.std])
print(df)

df = grouped["Points"].agg([np.sum, np.mean, np.std])
print(df)

# NaN값이 있다면 .fillna(0)으로 제거