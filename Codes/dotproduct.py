import numpy as np

a = np.array([[-2,3],[4,5]])
b = np.array([[-0.22727273,  0.13636364],
               [ 0.18181818,  0.09090909]])
inverse = np.linalg.inv(a)
print(inverse)
dotproduct = np.dot(a, b)
print(dotproduct)