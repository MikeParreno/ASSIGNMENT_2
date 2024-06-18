import numpy as np

#1
A = np.array([[1, 2, 3], [4, 5, 6]])
flattened_A = A.flatten()
print("Example 1 - Flattened Matrix:")
print(flattened_A)
#2
B = np.array([[5, 2], [3, 9]])
C = np.array([[7, 6], [3, 8]])

E = np.dot(B, C)

result = E.flatten()
print(f'Example 2 - {result}')
#3 
import numpy as np 

A = np.array([[[1, 23, 32], [42, 5, 16]], [[7, 68, 9], [10, 11, 12]]])

A_flat = A.flatten(order='F')  # 'F' order (column-major)
print("Example 3 - Flattened array with 'F' order:")
print(A_flat)

