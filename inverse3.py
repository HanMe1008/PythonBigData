import numpy as np

A = np.array([[1, 1], [2, 4]])
b = np.array([[7], [22]])

A_inv = np.linalg.inv(A)

X = A_inv @ b 

print(X)
