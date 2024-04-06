# vector 전치행렬
import numpy as np
A = np.array([1, 2, 3, 4, 5, 6])
B = A.T

C = A.reshape(1, 6)     # 1x6 matrix
D = C.T

print("A.shape ==", A.shape, ", B.shape ==", B.shape)
print("C.shape ==", C.shape, ", D.shape ==", D.shape)
print(D)