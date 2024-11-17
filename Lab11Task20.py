import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
inverse = np.linalg.inv(np.dot(a.T, a))
identity_check = np.dot(inverse, np.dot(a.T, a))
print("\nДобуток (a^T * a)^-1 * (a^T * a):")
print(identity_check)