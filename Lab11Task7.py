import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
sorted_cols = np.sort(a, axis=0)
print("\nМасив а за зростанням у стовпцях:")
print(sorted_cols)