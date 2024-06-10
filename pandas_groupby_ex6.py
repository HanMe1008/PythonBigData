import pandas as pd
import numpy as np
df_phone = pd.read_csv("F:/PythonBigData/phone_data.csv")
import dateutil
df_phone['date'] = df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)

# 1개 column에도 여러 개의 aggregtaion
# nunique() : 데이터에 고유값들의 수를 출력해주는 함수
# unique()  : 데이터에 고유값들이 어떠한 종류인지 파악하는 함수
df_phone = df_phone.groupby(['month', 'item']).agg({"duration" : "sum",
                                                    "network_type" : "count",
                                                    "date" : [min, 'first', 'nunique']})
print(df_phone)