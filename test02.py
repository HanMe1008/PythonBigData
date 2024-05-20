import numpy as np

# 행렬 만들기
A1 = np.array([1, 2, 3, 4]).reshape(2, 2)
A2 = np.arange(1, 5).reshape(2, 2)

# 전치행렬
A1.T

# 역행렬 
B = np.linalg.inv(A1)

# 행렬합치기
a = np.concatenate([A1, A2], axis=0)    # 세로
b = np.concatenate([A1, A2], axis=1)    # 가로

# 행렬자르기
b_left, b_right = np.split(b, [2], axis=1)

# 축확장
m = np.array([0.0, 10.0, 20.0, 30.0])
n = np.array([1.0, 2.0, 3.0])
print(m[:, np.newaxis]+n)

# 1~9까지 랜덤 3x3 행렬
xx = np.random.randint(1, 10, size=[3, 3])  