import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
reordered_rows = a[[1, 2, 0], :]
print("\nРядки масиву а у порядку 2й, 3й, 1й:")
print(reordered_rows)