import pandas as pd
import numpy as np
df_phone = pd.read_csv("F:/PythonBigData/phone_data.csv")
import dateutil
df_phone['date'] = df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)

# 2개 항목 추출 -> aggregation 형태
# as_index=False : index를 따로 만들어 사용
df_phone = df_phone.groupby('month', as_index=False).agg({"duration":"sum"})
print(df_phone)

df_phone = df_phone.groupby('month').agg({"duration":"sum"})
print(df_phone)