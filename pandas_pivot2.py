import pandas as pd
col = ['Machine', 'Country', 'Price', 'Brand']
data = [['TV', 'Korea', 1000, 'A'],
        ['TV', 'Japan', 1100, 'B'],
        ['TV', 'China',  300, 'C'],
        ['PC', 'Korea', 3000, 'A'],
        ['PC', 'Japan', 2000, 'E'],
        ['PC', 'China',  800, 'F']]
df = pd.DataFrame(data=data, columns=col)
# 다중 인덱스
#df = df.pivot(index=['Country', 'Machine'], columns='Brand', values='Price')
df = df.pivot(index='Country', columns=['Machine', 'Brand'], values='Price')

print(df)