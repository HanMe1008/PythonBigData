import pandas as pd
df1 = pd.DataFrame([1], inde=['a'])
df2 = pd.DataFrame([2], inde=['a'])
#df = pd.concat([df1, df2], verify_integrity=True)
df = pd.concat([df1, df2])
print(df)