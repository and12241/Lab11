import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
selected_elements = a[[0, 2, 1], [3, 2, 2]]
print("\nВибрані елементи:")
print(selected_elements)
