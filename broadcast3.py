import numpy as np

a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([1.0, 2.0, 3.0])

# 축 확장
print(a[:, np.newaxis]+b)