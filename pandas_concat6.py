import pandas as pd
df1 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']],
                   columns=['animal', 'name'])
print(df1)

df2 = pd.DataFrame([['a', 1.], ['b', 2]],
                   columns=['letter', 'number'])
print(df2)

df3 = pd.concat([df1, df2], axis=1)
print(df3)