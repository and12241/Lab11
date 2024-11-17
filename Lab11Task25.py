import numpy as np
coeff_matrix = np.array([[1, 2], [3, 4]])
results = np.array([5, 6])
solution = np.linalg.solve(coeff_matrix, results)
print("\nРозв’язок системи рівнянь:")
print(solution)