import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

def inverse(matrix):
    return np.linalg.inv(matrix)

# Example usage
matrix = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [5, 6, 0]])

det = determinant(matrix)
inv = inverse(matrix) if det != 0 else None

print("Determinant:", det)
print("Inverse:\n", inv)
