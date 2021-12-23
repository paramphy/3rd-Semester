import numpy as np

A = np.array([[ 2,  4,  6],
                [ 1, -3, -9],
                [ 8,  5, -7]])

lam, evec = np.linalg.eig(A)
#print(lam)
#print(evec)
print(lam[0])
print(evec[:,0])