import numpy as np

# dot method
#1
arr1= np.array([[6, 2], [1, 4]])
arr2 = np.array([[5, 6], [8, 8]])
dot_result_1 = np.dot(arr1, arr2)
print("Example 1")
print(dot_result_1)
#2
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4= np.array([[7, 8], [9, 10], [11, 12]])
dot_result_2 = np.dot(arr3, arr4)
print("\nExample 2")
print(dot_result_2)
#3 
A = np.array([[1, 2, 1], [9, 1, 4], [6, 4, 10]])
B = np.array([[5, 10, 6], [7, 4, 8], [8, 7, 1]])
C = np.array([[9, 10, 12], [11, 0, 12], [9, 0, 7]])
dot_result_3 = np.dot(np.dot(A, B), C)
print("Example 3")
print(dot_result_3)