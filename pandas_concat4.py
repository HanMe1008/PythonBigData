import pandas as pd
df1 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
                     columns=['letter', 'number', 'animal'])
print(df1)

df2 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])
print(df2)

df3 = pd.concat([df1, df2])
print(df3)