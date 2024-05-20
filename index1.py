import numpy as np

A = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14 ,15],
              [-1, -2, -3, -4, -5]])

# 행변환
idx = [1, 2, 0, 3]
# what_i_want = A[ [1, 2, 0, 3], : ]
result = A[idx, :]
print(result)

