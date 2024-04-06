import numpy as np

A = np.array([[15, 5], [0, -5]])  # 2x2 행렬
B = np.array([[10, -5], [5, 15]])  # 2x2 행렬

X = A + 2*B
Y = B - 2*A

print(X)
print("------------------------------")
print(Y)