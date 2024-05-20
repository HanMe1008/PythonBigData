import numpy as np

array1 = np.arange(6).reshape(2, 3) # (2x3)
array2 = np.arange(2).reshape(2, 1) # (2x1)
array3 = array1 + array2
print(array3)
