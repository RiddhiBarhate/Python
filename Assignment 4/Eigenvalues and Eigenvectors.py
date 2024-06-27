import numpy as np

def find_eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Example usage
matrix = np.array([[4, -2],
                   [1,  1]])

eigenvalues, eigenvectors = find_eigen(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
