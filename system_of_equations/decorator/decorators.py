import numpy as np
from system_of_equations.errors.exceptions import NonSquareMatrixError, SingularMatrixError, InvalidMatrixStructureError



def check_square(func):
    def wrapper(matrix, *args, **kwargs):
        if matrix.shape[0] != matrix.shape[1]:
            raise NonSquareMatrixError(matrix)
        return func(matrix, *args, **kwargs)
    return wrapper

def check_singular(func):
    def wrapper(matrix, *args, **kwargs):
        if np.linalg.det(matrix) == 0:
            raise SingularMatrixError()
        return func(matrix, *args, **kwargs)
    return wrapper

def check_tridiagonal(func):
    def wrapper(matrix, *args, **kwargs):
        off_diagonal_sum = sum(abs(matrix[i, j]) for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) if abs(i-j) > 1)
        if off_diagonal_sum != 0:
            raise InvalidMatrixStructureError(matrix, "tridiagonal")
        return func(matrix, *args, **kwargs)
    return wrapper
