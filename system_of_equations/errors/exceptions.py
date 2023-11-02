class LinearEquationError(Exception):
    """Base class for linear system errors."""
    pass

class NonSquareMatrixError(LinearEquationError):
    """Error for cases when the matrix is not square."""
    def __init__(self, matrix):
        self.matrix = matrix
        super().__init__(f"Matrix of shape {matrix.shape} is not square!")

class SingularMatrixError(LinearEquationError):
    """Error for cases when the matrix is singular (undefined or degenerate)."""
    def __init__(self):
        super().__init__("Matrix is singular or degenerate!")

class IterationDivergenceError(LinearEquationError):
    """Error indicating divergence of the iteration method."""
    def __init__(self, max_iterations):
        super().__init__(f"Iteration method is divergent after {max_iterations} iterations!")

class InvalidMatrixStructureError(LinearEquationError):
    """Error for cases when the matrix does not match the expected structure."""
    def __init__(self, matrix, expected_type):
        self.matrix = matrix
        super().__init__(f"Matrix does not match the expected structure: {expected_type}")

class ConvergenceError(LinearEquationError):
    """Error indicating convergence issues of the method."""
    def __init__(self):
        super().__init__("Convergence issues with the method!")
