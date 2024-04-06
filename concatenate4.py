import numpy as np

A = np.array([[10, 20, 30], [40, 50, 60]])
print(A.shape)

column_add = np.array([1000, 2000]).reshape(2, 1)
print(column_add.shape)

C = np.concatenate((A, column_add), axis=1)
print(C)