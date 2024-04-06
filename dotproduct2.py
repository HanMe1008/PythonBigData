import numpy as np

x = np.array([[1, 1],
              [2, 4]])
y = np.array([[7],
              [22]])

result = np.linalg.inv(x) @ y
print(result)
