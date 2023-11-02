import numpy as np
from system_of_equations.errors.exceptions import NonSquareMatrixError, SingularMatrixError, InvalidMatrixStructureError

def check_square(func):
    """
    A decorator that checks if the input matrix is square before executing the decorated function.

    Parameters:
    - func (callable): The function to be decorated, which operates on a square matrix.

    Raises:
    - NonSquareMatrixError: If the input matrix is not square (i.e., the number of rows is not equal to the number of columns).

    Returns:
    - callable: A decorated function that operates on a square matrix.
    """
    def wrapper(matrix, *args, **kwargs):
        if matrix.shape[0] != matrix.shape[1]:
            raise NonSquareMatrixError(matrix)
        return func(matrix, *args, **kwargs)
    return wrapper

def check_singular(func):
    """
    A decorator that checks if the input matrix is singular (non-invertible) before executing the decorated function.

    Parameters:
    - func (callable): The function to be decorated, which operates on a non-singular matrix.

    Raises:
    - SingularMatrixError: If the input matrix is singular (i.e., its determinant is zero).

    Returns:
    - callable: A decorated function that operates on a non-singular matrix.
    """
    def wrapper(matrix, *args, **kwargs):
        if np.linalg.det(matrix) == 0:
            raise SingularMatrixError()
        return func(matrix, *args, **kwargs)
    return wrapper

def check_tridiagonal(func):
    """
    A decorator that checks if the input matrix has a tridiagonal structure before executing the decorated function.

    Parameters:
    - func (callable): The function to be decorated, which operates on a tridiagonal matrix.

    Raises:
    - InvalidMatrixStructureError: If the input matrix does not have a tridiagonal structure.

    Returns:
    - callable: A decorated function that operates on a tridiagonal matrix.
    """
    def wrapper(matrix, *args, **kwargs):
        off_diagonal_sum = sum(abs(matrix[i, j]) for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) if abs(i-j) > 1)
        if off_diagonal_sum != 0:
            raise InvalidMatrixStructureError(matrix, "tridiagonal")
        return func(matrix, *args, **kwargs)
    return wrapper