import numpy as np

x = np.array([[1, 1], [2, 4]])
y = np.linalg.inv(x)
z = np.array([[7], [22]])

# 1~9까지 랜덤 3x3 행렬
xx = np.random.randint(1, 10, size=[3, 3])  

print(y @ z)

print(xx)
