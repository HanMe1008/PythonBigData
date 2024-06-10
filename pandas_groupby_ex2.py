import pandas as pd
import numpy as np
df_phone = pd.read_csv("F:/PythonBigData/phone_data.csv")
import dateutil
df_phone['date'] = df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)
#df = df_phone.head()
print(df_phone)

df_phone = df_phone.groupby('month')['duration'].sum()
print(df_phone)