import numpy as np

A = np.array([0, 1, 2, 3, 4, 5, 6, 7]).reshape(2, 4)
B = np.arange(8).reshape(2, 4)

# concatenate
C = np.concatenate((A, B), axis=0)
print(C)
print()

D = np.array([1, 2, 3, 4]).reshape(4, 1)
# D = np.arange(1, 5).reshape(4, 1)

# broadcast
print(C + D)