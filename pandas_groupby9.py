import pandas as pd
import numpy as np
ipl_data = {'Team'  : ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'Kings',
                       'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank'  : [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            'Year'  : [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
            'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)
print(df)

#df = df.groupby("Team").filter(lambda x: len(x) >= 3)
#print(df)

#df = df.groupby("Team").filter(lambda x: x["Points"].sum() >= 3000)
#print(df)

#df = df.groupby("Team").filter(lambda x: x["Points"].mean() > 700)
#print(df)

df = df.groupby("Team").filter(lambda x: x["Points"].mean() > 800)
print(df)

#df = df.groupby("Team").filter(lambda x: x["Points"].max() > 850)
#print(df)
