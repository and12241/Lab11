import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
sorted_rows = np.sort(a, axis=1)
print("\n\nМасив а за зростанням у рядках:")
print(sorted_rows)