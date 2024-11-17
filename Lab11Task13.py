import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
b = a.reshape(2, 6)
print("\nМасив b розміром 2x6:")
print(b)
c = b.T
print("\nТранспонований масив c:")
print(c)
identity_column = np.ones((c.shape[0], 1))
d = np.hstack((identity_column, c))
print("\nМасив d (з одиничним стовпцем):")
print(d)
d1, d2 = np.hsplit(d, [2])
print("\nПерший масив після розрізання:")
print(d1)
print("\nДругий масив після розрізання:")
print(d2)