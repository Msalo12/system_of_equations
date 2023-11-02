import numpy as np  # You can use numpy for matrix operations
import sys
from matrix import Matrix

class MatrixInversion:
    def __init__(self, matrix):
        self.matrix = matrix

    def inverse(self):
        raise NotImplementedError("Inverse method must be implemented by child classes")

class GaussMatrixInversion(MatrixInversion):
    def inverse(self):
        # Implement matrix inversion using Gauss method
        if np.linalg.matrix_rank(self.matrix.data) != self.matrix.rows:
            raise ValueError("Matrix is singular, cannot be inverted using Gauss method")
        
        n = self.matrix.rows
        a = np.array(self.matrix.data, dtype=float)

        # Augment with identity matrix
        identity = np.identity(n)
        a = np.concatenate((a, identity), axis=1)

        for i in range(n):
            if a[i][i] == 0.0:
                sys.exit('Divide by zero detected!')

            for j in range(n):
                if i != j:
                    ratio = a[j][i] / a[i][i]
                    a[j] -= ratio * a[i]

        for i in range(n):
            a[i] /= a[i][i]

        inverted_data = a[:, n:]
        return Matrix(n, n, inverted_data.tolist())

class AlgebraicMatrixInversion(MatrixInversion):
    def inverse(self):
        # Implement matrix inversion using the matrix of algebraic additions (adjugate matrix)
        if np.linalg.matrix_rank(self.matrix.data) != self.matrix.rows:
            raise ValueError("Matrix is singular, cannot be inverted using the adjugate matrix method")
        
        # Your implementation of the adjugate matrix method for inversion here
        adjugate_matrix = np.linalg.inv(self.matrix.data)
        inverted_matrix = np.linalg.det(self.matrix.data) * adjugate_matrix
        return Matrix(self.matrix.rows, self.matrix.columns, inverted_matrix.tolist())


matrix_data = [
    [1, 1, 3],
    [1, 3, -3],
    [-2, -4, -4],
]

matrix_instance = Matrix(3, 3, matrix_data)

# Using GaussMatrixInversion
gauss_inverter = GaussMatrixInversion(matrix_instance)
gauss_inverse_matrix = gauss_inverter.inverse()

print("Inverse Matrix using Gauss method:")
print(gauss_inverse_matrix)

