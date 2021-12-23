import numpy as np

A = np.array([[2, 4, 6], [1, -3, -9], [8, 5, -7]])
b = np.array([4, -11, 2])
solution = np.linalg.solve(A,b)
print(solution)

# Another method
Ainv = np.linalg.inv(A)
solution = np.dot(Ainv,b)
print(solution)