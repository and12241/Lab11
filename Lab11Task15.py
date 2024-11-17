import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
bottom_right = a[-2:, -2:]
print("\nМасив 2x2 з нижнього правого кута:")
print(bottom_right)