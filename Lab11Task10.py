import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
b = a.reshape(2, 6)
print("\nМасив b розміром 2x6:")
print(b)