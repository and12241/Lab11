import numpy as np
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
diagonal_elements = np.diag(np.dot(a.T, a))
print("\nДіагональні елементи матриці a^T * a:")
print(diagonal_elements)
inverse = np.linalg.inv(np.dot(a.T, a))
diagonal_sum = np.sum(diagonal_elements)
y = np.array([1, 2, 3])
d = np.dot(inverse, np.dot(a.T, y))
print("\nРезультат обчислення d:")
print(d)