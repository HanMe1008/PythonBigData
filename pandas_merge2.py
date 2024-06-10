import pandas as pd
raw_data1 = {'subject_id':['1','2','3','4','5','7','8','9','10','11'],
            'test_score':[51,15,15,61,16,14,15,1,61,16]}
df_a = pd.DataFrame(raw_data1,
                    columns=['subject_id', 'test_score'])
print(df_a)

raw_data2 = {'subject_id':['4','5','6','7','8'],
             'first_name':['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
             'last_name' :['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data2,
                    columns=['subject_id', 'first_name', 'last_name'])
print(df_b)

## Join Method : left join ##
# 기준 df_a에 df_b를 첨가 (df_a에 없는 것 --> NaN)
df1 = pd.merge(df_a, df_b, on='subject_id', how='left')
print(df1)

# NaN 처리 (.fillna(0))
df1 = pd.merge(df_a, df_b, on='subject_id', how='left').fillna(0)
print(df1)

## Join Method : how='right' ##
df2 = pd.merge(df_a, df_b, on='subject_id', how='right')
print(df2)

## Join Method : how='outer' ##
# df_a / df_b 양쪽 다 출력
# column에 value 있으면 합쳐줌, 없으면 NaN
df3 = pd.merge(df_a, df_b, on='subject_id', how='outer')
print(df3)

## Index based join ##
# 같은 index끼리 합침
# key, value가 있는 column(값)이 존재하지 않을 경우는
# index를 기준으로 join이 됨
df4 = pd.merge(df_a, df_b, right_index=True, left_index=True)
print(df4)