import numpy as np

A = np.array([[ 1,  2,  3,  4,  5],
              [ 6,  7,  8,  9, 10],
              [11, 12, 13, 14, 15],
              [-1, -2, -3, -4, -5]])

# [[13 12 14]
#  [-3 -2 -4]
#  [ 3  2  4]] 를 출력하기 위해선
idx_r = [2, 3, 0]
idx_c = [2, 1, 3]

result = A[idx_r, :][:,idx_c]

print(result)