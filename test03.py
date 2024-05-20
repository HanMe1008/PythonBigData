# 1번문제

# list연산
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[-1, -2, -3],
     [-4, -5, -6]]
print("list연산")
print(A+B)

# numpy 연산
import numpy as np 

A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[-1, -2, -3],
              [-4, -5, -6]])
print("numpy연산")
print(A+B)

print()

# 2번 문제
A = np.arange(15)
print("1차원 행렬")
print(A)

A = np.arange(15).reshape(3, 5)
print("2차원 행렬")
print(A)

print()


# 3번 문제
# (1)
A = np.arange(8).reshape(2, 4)
B = np.arange(8).reshape(2, 4)
print("A =", A)
print("B =", B)

# (2)
C = np.concatenate([A, B], axis=0)
print("C =", C)

# (3)
print(C < 5)

# (4)
C[C < 5] = 100
print(C)

print()

# 4번 문제
# (1)
A = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [-1, -2, -3, -4, -5]])
print("A =", A)

# (2)
idx_r = [2, 3, 0, 0]
idx_c = [2, 1, 3, 4]

B1 = A[idx_r, :][:, idx_c]
print("B1 =", B1)

# (3)
B2 = A[idx_r, idx_c]
print("B2 =", B2)

print()

