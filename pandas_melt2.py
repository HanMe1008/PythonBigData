import pandas as pd

df = pd.DataFrame({'A': {0:'a', 1:'b', 2:'c'},
                   'B': {0:1, 1:3, 2:5},
                   'C': {0:2, 1:4, 2:6}})
print(df)
#df = pd.melt(df, id_vars=['A'], value_vars=['B', 'C'], ignore_index=False)
df.columns = [list('ABC'), list('DEF')]
print(df)
#df = pd.melt(df, col_level=0, id_vars=['A'], value_vars=['B'])
df = pd.melt(df, id_vars=[('A', 'D')], value_vars=[('B', 'E')])
print(df)