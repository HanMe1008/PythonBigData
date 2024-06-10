import pandas as pd
import numpy as np
ipl_data = {'Team'  : ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'Kings',
                       'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank'  : [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            'Year'  : [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
            'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby("Team")
for name, group in grouped:
    print(name)
    print(group)

for data in grouped:
    print(data)

df = grouped.get_group("Devils")
print(df)
df = grouped.get_group("Riders")
print(df)