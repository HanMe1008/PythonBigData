import numpy as np

A = np.arange(0, 8).reshape(2, 4)
B = np.arange(0, 8).reshape(2, 4)

C = np.concatenate((A, B), axis=0)
print(C)

print(C<5)
