import pandas as pd
import numpy as np
df_phone = pd.read_csv("F:/PythonBigData/phone_data.csv")
import dateutil
df_phone['date'] = df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)

# 1개 이상의 groupby & aggregation 를 선택 할 경우
df_phone = df_phone.groupby(['month', 'item']).agg({"duration" : "sum",
                                                    "network_type" : "count",
                                                    "date" : "first"})
print(df_phone)