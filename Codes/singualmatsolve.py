import numpy as np

A = np.array([[ 2,  4,  6],
                [ 1, -3, -9],
                [ 1,  2,  3]])

b = np.array([4, -11, 2])
solution = np.linalg.solve(A,b)
# using alternate method
Ainv = np.linalg.inv(A)