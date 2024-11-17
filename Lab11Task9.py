import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
reversed_cols = a[:, ::-1]
print("\nСтовпці масиву а у зворотному порядку:")
print(reversed_cols)