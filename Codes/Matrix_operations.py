# Addition of Two Matrices
import numpy as np
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A + B # element wise addition
print(C)

print('-----------------------------------------------')

# Multiplication of Two Matrices
import numpy as np
A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
print(C)
print('-----------------------------------------------')

# Transpose of a Matrix

import numpy as np
A = np.array([[1, 1], [2, 1], [3, -3]])
print(A.transpose())
print('-----------------------------------------------')