import numpy as np

A = np.array([[1, 2], [3, 4]])  # 2x2 행렬
B = np.array([[5, 6], [7, 8]])  # 2x2 행렬

X = B - A
Y = A - B

print(X)
print("----------------------------")
print(Y)