import pandas as pd
import numpy as np
df_phone = pd.read_csv("F:/PythonBigData/phone_data.csv")
import dateutil
df_phone['date'] = df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)

# 1개 column name 내의 해당 항목의 사용량
df_phone1 = df_phone[df_phone['item']=='call'].groupby('network')['duration'].sum()
print(df_phone1)
df_phone2 = df_phone[df_phone['item']=='call'].groupby('month')['duration'].sum()
print(df_phone2)

# 2개 column names 선택
df_phone3 = df_phone.groupby(['item', 'month'])['duration'].sum()
print(df_phone3)

df_phone4 = df_phone.groupby(['month', 'item'])['duration'].sum()
print(df_phone4)

df_phone5 = df_phone.groupby(['month', 'item'])['network'].count()
print(df_phone5)

df_phone6 = df_phone.groupby(['month', 'item'])['date'].count()
print(df_phone6)

# 2개 항목 추출 -> matrix 형태 (.unstack())
df_phone7 = df_phone.groupby(['month', 'item'])['date'].count().unstack()
print(df_phone7)


