import numpy as np

# Modified four-node network with a different connection pattern.
A = np.array([
    [0., 1., 0., 1.],
    [1., 0., 1., 1.],
    [0., 1., 0., 1.],
    [1., 1., 1., 0.]
])
nodes = ["Database", "API", "Worker", "Gateway"]

eigenvalues, eigenvectors = np.linalg.eig(A)
index = np.argmax(np.abs(np.real(eigenvalues)))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

print("Modified network dominant eigenvalue:", dominant_value)
print("Modified eigenvector-based importance:")
for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

v = np.real(eigenvectors[:, index])
print("Verification error:",
      np.linalg.norm(A @ v - dominant_value * v))