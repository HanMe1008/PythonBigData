import numpy as np

A = np.array([[10, 20, 30], [40, 50, 60]])
print(A.shape)


# 처음부터 row_add = np.array([[70, 80, 90]])로 행렬을 만들면 안되나?
row_add = np.array([70, 80, 90]).reshape(1, 3)
print(row_add.shape)

B = np.concatenate((A, row_add), axis=0)
print(B)