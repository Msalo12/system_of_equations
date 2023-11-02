class LinearEquationError(Exception):
    """Base class for linear system errors."""
    pass

class NonSquareMatrixError(LinearEquationError):
    """Error for cases when the matrix is not square."""
    def __init__(self, matrix):
        """Initialize NonSquareMatrixError with a non-square matrix.

        Args:
            matrix (ndarray): The non-square matrix that caused the error.
        """
        self.matrix = matrix
        super().__init__(f"Matrix of shape {matrix.shape} is not square!")

class SingularMatrixError(LinearEquationError):
    """Error for cases when the matrix is singular (undefined or degenerate)."""
    def __init__(self):
        """Initialize SingularMatrixError."""
        super().__init__("Matrix is singular or degenerate!")

class IterationDivergenceError(LinearEquationError):
    """Error indicating divergence of the iteration method."""
    def __init__(self, max_iterations):
        """Initialize IterationDivergenceError with the maximum number of iterations.

        Args:
            max_iterations (int): The maximum number of iterations attempted before divergence.
        """
        super().__init__(f"Iteration method is divergent after {max_iterations} iterations!")

class InvalidMatrixStructureError(LinearEquationError):
    """Error for cases when the matrix does not match the expected structure."""
    def __init__(self, matrix, expected_type):
        """Initialize InvalidMatrixStructureError with a matrix and its expected structure.

        Args:
            matrix (ndarray): The matrix that does not match the expected structure.
            expected_type (str): The expected structure description.
        """
        self.matrix = matrix
        super().__init(f"Matrix does not match the expected structure: {expected_type}")

class ConvergenceError(LinearEquationError):
    """Error indicating convergence issues of the method."""
    def __init__(self):
        """Initialize ConvergenceError."""
        super().__init__("Convergence issues with the method!")
