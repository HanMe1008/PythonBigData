import numpy as np

A=np.arange(29, -1, -1).reshape(2, 3, 5)
print(A)

print("")
print("----------------------------------------")
print("")

B=np.arange(30).reshape(2, 3, 5)
print(B)

print(B[0][1][3])