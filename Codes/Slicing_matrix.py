# Slicing of a list
import numpy as np
letters = np.array([1, 3, 5, 7, 9, 7, 5])
# 3rd to 5th elements
print(letters[2:5]) # Output: [5, 7, 9]
# 1st to 4th elements
print(letters[:-5]) # Output: [1, 3]
# 6th to last elements
print(letters[5:]) # Output:[7, 5]
# 1st to last elements
print(letters[:]) # Output:[1, 3, 5, 7, 9, 7, 5]
# reversing a list
print(letters[::-1]) # Output:[5, 7, 9, 7, 5, 3, 1]
print('--------------------------------------------------')

# Slicing of a matrix
import numpy as np
A = np.array([[1, 4, 5, 12, 14],
[-5, 8, 9, 0, 17],
[-6, 7, 11, 19, 21]])
print(A[:2, :4]) # two rows, four columns
print(A[:1,]) # first row, all columns
print(A[:,2]) # all rows, second column
print(A[:, 2:5]) # all rows, third to the fifth column