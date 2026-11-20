import numpy as np

a = 0.2
b = 0.1
calculated = a + b
expected = 0.3

print("0.2 + 0.1 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))

true_value = np.sqrt(2)
approx_value = 1.4142
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
print(f"Absolute error: {absolute_error:.10f}")
print(f"Relative error: {relative_error:.8%}")