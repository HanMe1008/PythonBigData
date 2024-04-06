import numpy as np

a = np.array([[ 0.0, 0.0, 0.0],     # (4x3)
              [10.0, 10.0, 10.0],
              [20.0, 20.0, 20.0],
              [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])       # (1x3)

print(a+b)
print()

print(a-b)
print()

print(a*b)
print()

print(a/b)
print()

print(a@b)