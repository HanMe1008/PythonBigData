import numpy as np

array1 = np.arange(4).reshape(2, 2) # (2x2)
array2 = np.arange(2)   # (1x2)
array3 = array1 + array2
print(array3)