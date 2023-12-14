import numpy as np
import sys
from system_of_equations.matrix_operations.matrix import Matrix

class MatrixInversion:
    """
    Abstract base class for matrix inversion methods.

    Attributes:
    - matrix: The matrix to be inverted.

    Methods:
    - inverse(self): Computes the inverse of the matrix. Subclasses must implement this method.
    """
    def __init__(self, matrix):
        """
        Initialize the MatrixInversion instance.

        Parameters:
        - matrix: The matrix to be inverted.
        """
        self.matrix = matrix

    def inverse(self):
        """
        Compute the inverse of the matrix.

        Raises:
        NotImplementedError: This method must be implemented by child classes.
        """
        raise NotImplementedError("Inverse method must be implemented by child classes")

class GaussMatrixInversion(MatrixInversion):
    """
    Matrix inversion using the Gauss elimination method.

    Attributes:
    - matrix: The matrix to be inverted.

    Methods:
    - inverse(self): Computes the inverse of the matrix using the Gauss elimination method.

    Raises:
    ValueError: If the matrix is singular and cannot be inverted.
    """
    def inverse(self):
        """
        Compute the inverse of the matrix using the Gauss elimination method.

        Returns:
        A Matrix instance representing the inverted matrix.

        Raises:
        ValueError: If the matrix is singular and cannot be inverted.
        """
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
    """
    Matrix inversion using the matrix of algebraic additions (adjugate matrix) method.

    Attributes:
    - matrix: The matrix to be inverted.

    Methods:
    - inverse(self): Computes the inverse of the matrix using the adjugate matrix method.

    Raises:
    ValueError: If the matrix is singular and cannot be inverted.
    """
    def inverse(self):
        """
        Compute the inverse of the matrix using the adjugate matrix method.

        Returns:
        A Matrix instance representing the inverted matrix.

        Raises:
        ValueError: If the matrix is singular and cannot be inverted.
        """
        if np.linalg.matrix_rank(self.matrix.data) != self.matrix.rows:
            raise ValueError("Matrix is singular, cannot be inverted using the adjugate matrix method")
        
        n = self.matrix.rows
        adjugate_matrix = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                minor = np.delete(np.delete(self.matrix.data, i, axis=0), j, axis=1)
                cofactor = (-1) ** (i + j) * np.linalg.det(minor)
                adjugate_matrix[j, i] = cofactor

        determinant = np.linalg.det(self.matrix.data)
        
        if determinant == 0:
            raise ValueError("The matrix is singular and cannot be inverted.")
        
        inverted_matrix = adjugate_matrix / determinant
        inverted_matrix_rounded = np.round(inverted_matrix, 2)

        return Matrix(self.matrix.rows, self.matrix.columns, inverted_matrix_rounded.tolist())