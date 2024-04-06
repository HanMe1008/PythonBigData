import numpy as np

A = np.array([[ 1,  2,  3,  4,  5],
              [ 6,  7,  8,  9, 10],
              [11, 12, 13, 14, 15],
              [-1, -2, -3, -4, -5]])

# 행변환
idx = [4, 1, 2]
what_i_want = A[:, idx]
print(what_i_want)