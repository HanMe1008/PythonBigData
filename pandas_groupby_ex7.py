import pandas as pd
import numpy as np
df_phone = pd.read_csv("F:/PythonBigData/phone_data.csv")
import dateutil
df_phone['date'] = df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)

# column name -> column name 제거
# droplevel() : columns 제거
# rename() : new columns name 생성
grouped = df_phone.groupby('month').agg({"duration":[min, max, np.mean]})
grouped.columns = grouped.columns.droplevel(level=0)
df = grouped.rename(columns={"min": "min_duration", "max": "max_duration", "mean": "mean_duration"})

print(grouped)
print(df)

# rename 대신 add_prefix() 사용
df2 = grouped.add_prefix("duration")
print(df2)