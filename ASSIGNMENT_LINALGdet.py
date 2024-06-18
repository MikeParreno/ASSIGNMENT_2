import numpy as np
from numpy.linalg import det

#1
# Define a matrix
A = np.array([[11, 22], [33, 44]])

result = det(A)

print(f'Examle 1 - {result}')

#2
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

det_A = np.linalg.det(A)
print("Example 2 - Determinant of matrix A:")
print(det_A)

#3 
B = np.array([[5, 6], [7, 8]])
det_B = np.linalg.det(B)
print("\nExample 3 - Determinant of B:")
print(det_B)
