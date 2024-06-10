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

# 1) how='inner' : 양쪽 공통인 것만 출력
df1 = pd.merge(df_a, df_b, on='subject_id', how='inner')
print(df1)

# 2) 지정을 해주지 않고 merge 함수를 호출하면 Inner Join
df2 = pd.merge(df_a, df_b, on='subject_id')
print(df2)

# 3) left_on='subject_id', right_on='subject_id' : 위 결과와 동일
df3 = pd.merge(df_a, df_b, left_on='subject_id', right_on='subject_id')
print(df3)
