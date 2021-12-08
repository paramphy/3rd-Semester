# Array of integers, floats, and complex Numbers
import numpy as np
A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)
A = np.array([[1.1, 2, 3], [3, 4, 5]]) # Array of floats
print(A)
A = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) # Array of complex numbers
print(A)
print('-------------------------------------------')
# Array of zeros and ones
import numpy as np
zeors_array = np.zeros( (2, 3) )
print(zeors_array)

ones_array = np.ones( (1, 5), dtype=np.int32 ) # specifying dtype
print(ones_array) # Output: [[1 1 1 1 1]]
print("------------------------------------------")

# Using arange() and shape()

import numpy as np
A = np.arange(4)
print('A =', A)
B = np.arange(12).reshape(2, 6)
print('B =', B)
print('-----------------------------------------')