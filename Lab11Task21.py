import numpy as np
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
det = np.linalg.det(np.dot(a.T, a))
print("\nВизначник матриці a^T * a:")
print(det)