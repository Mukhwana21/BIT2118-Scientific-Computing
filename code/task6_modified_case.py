import numpy as np

# Type A: 5 CPU units and 6 GB memory
# Type B: 3 CPU units and 10 GB memory
A = np.array([
    [5.0, 3.0],
    [6.0, 10.0]
])
b = np.array([31.0, 86.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual norm:", np.linalg.norm(residual))