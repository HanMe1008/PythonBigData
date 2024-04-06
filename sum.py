import numpy as np

matrix = np.arange(15).reshape(3, 5)
print(matrix)
print(np.sum(matrix))
print()

# 각 열합
print(np.sum(matrix, axis=0))
print()

# 각 행합
print(np.sum(matrix, axis=1))
print()

# 5보다 큰 것만 출력
print(matrix[matrix > 5])
print()

# 마스킹
mask = matrix % 2 == 0
print(mask)
print()

# 짝수만 출력
print(matrix[matrix % 2 == 0])
print()

# Matrix 원소 7에 접근
print(matrix[1][2])
print(matrix[1, 2])