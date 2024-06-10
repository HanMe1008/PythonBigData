### 시험출제가능 ###
import pandas as pd        
col = ['Machine', 'Country', 'Price', 'Brand']
data = [['TV', 'Korea', 1000, 'A'],
        ['TV', 'Japan', 1100, 'B'],
        ['TV', 'China',  300, 'C'],
        ['PC', 'Korea', 3000, 'A'],
        ['PC', 'Japan', 2000, 'E'],
        ['PC', 'China',  800, 'F']]
df = pd.DataFrame(data=data, columns=col)
#df = df.pivot(index='Machine', columns='Country', values='Price')
df = df.pivot(index='Machine', columns='Country', values=['Price', 'Brand'])
#df = df.pivot(index='Machine', columns='Country') # 위 실행결과와 동일
#df = df.pivot(index='Machine', columns='Country')['Brand']

print(df)