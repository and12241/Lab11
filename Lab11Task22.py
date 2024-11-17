import numpy as np
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
diagonal_elements = np.diag(np.dot(a.T, a))
print("\nДіагональні елементи матриці a^T * a:")
print(diagonal_elements)