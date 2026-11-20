import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([
    [5.0, -1.0, 0.0],
    [-1.0, 5.0, -1.0],
    [0.0, -1.0, 4.0]
])
measurement_sets = [
    np.array([20.0, 12.0, 14.0]),
    np.array([18.0, 10.0, 16.0])
]

lu, piv = lu_factor(A)
for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    print(f"Measurement set {i}:")
    print("Solution:", x)
    print("Residual norm:", np.linalg.norm(b - A @ x))