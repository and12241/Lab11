import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
product = np.dot(a, a.T)
print("\nДобуток a * a^T:")
print(product)
