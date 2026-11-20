import numpy as np

temperatures_c = np.array([
    19.0, 18.8, 18.5, 18.7, 19.4, 20.5,
    22.2, 24.1, 26.0, 27.8, 29.2, 30.1,
    30.5, 30.0, 29.3, 28.1, 26.8, 25.2,
    23.9, 22.8, 21.5, 20.7, 20.0, 19.4
])

print(f"Daily mean temperature: {np.mean(temperatures_c):.2f} C")
print(f"Minimum temperature: {np.min(temperatures_c):.2f} C")
print(f"Maximum temperature: {np.max(temperatures_c):.2f} C")
print("Fahrenheit readings:", 1.8 * temperatures_c + 32)