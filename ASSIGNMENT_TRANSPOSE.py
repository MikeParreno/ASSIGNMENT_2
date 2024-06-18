import numpy as np

# Example 1: 2x3 matrix
A = np.array([[1, 2, 3],
              [4, 5, 6]])
A_transpose = np.transpose(A)
print("Example 1 - Transpose of Matrix A:")
print(A_transpose)

# Example 2: 3x2 matrix
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])
B_transpose = np.transpose(B)
print("\nExample 2 - Transpose of Matrix B:")
print(B_transpose)

# Example 3: 1D array
C = np.array([13, 14, 15, 16])
C_transpose = np.transpose(C)  # No effect on 1D array
print("\nExample 3 - Transpose of 1D Array C:")
print(C_transpose)
