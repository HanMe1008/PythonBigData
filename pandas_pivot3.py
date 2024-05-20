import pandas as pd
df2 = pd.DataFrame (data = [['A', 'x', 1],
            ['A', 'x', 2],
            ['B', 'y', 3],
            ['B', 'z', 4]],
            columns=['col1', 'col2', 'col3'])
print(df2)

# 오류발생 : 인덱스에 중복 항목이 포함되어 있어 모양 변경 불가능
print(df2.pivot(index='col1', columns='col2', values='col3'))