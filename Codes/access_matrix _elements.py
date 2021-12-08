# Access matrix elements
import numpy as np
A = np.array([2, 4, 6, 8, 10])
print("A[0] =", A[0]) # First element
print("A[2] =", A[2]) # Third element
print("A[-1] =", A[-1]) # Last element
print('----------------------------------------------')

# accessing two-dimensional array
import numpy as np
A = np.array([[1, 4, 5, 12],
[-5, 8, 9, 0],
[-6, 7, 11, 19]])
# First element of first row
print("A[0][0] =", A[0][0])
# Third element of second row
print("A[1][2] =", A[1][2])
# Last element of last row
print("A[-1][-1] =", A[-1][-1])
print('----------------------------------------------')
import numpy as np
A = np.array([[1, 4, 5, 12],
[-5, 8, 9, 0],
[-6, 7, 11, 19]])
print("A[0] =", A[0]) # First Row
print("A[2] =", A[2]) # Third Row
print("A[-1] =", A[-1]) # Last Row (3rd row in this case)
print('----------------------------------------------')
# Access columns of a Matrix
import numpy as np
A = np.array([[1, 4, 5, 12],
[-5, 8, 9, 0],
[-6, 7, 11, 19]])
print("A[:,0] =",A[:,0]) # First Column
print("A[:,3] =", A[:,3]) # Fourth Column
print("A[:,-1] =", A[:,-1]) # Last Column (4th column in this case)
print('------------------------------------------------------')
