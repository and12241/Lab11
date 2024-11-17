import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Масив а:")
print(a)
print("\nВсі елементи масиву а один за одним:")
for element in a.flat:
    print(element, end=" ")