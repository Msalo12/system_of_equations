import numpy as np
from system_of_equations.decorator.decorators import check_square, check_singular
class MatrixMethod:
    """
    A class for solving a system of linear equations using the matrix inversion method.

    Attributes:
    - coefficient_matrix: The coefficient matrix of the system of linear equations.
    - right_hand_side: The vector representing the right-hand side of the equations.

    Methods:
    - __init__(self, coefficient_matrix, right_hand_side): Initializes the solver with the coefficient matrix and right-hand side.
    - solve(self): Solves the system of linear equations using the matrix inversion method.

    Note:
    - The coefficient matrix must be square and non-singular for the matrix inversion method to work.
    - The method raises a ValueError if the coefficient matrix is singular.
    """

    def __init__(self, coefficient_matrix, right_hand_side):
        """
        Initializes the MatrixLinearSystemSolver instance.

        Parameters:
        - coefficient_matrix: The coefficient matrix of the system of linear equations.
        - right_hand_side: The vector representing the right-hand side of the equations.
        """
        self.coefficient_matrix = np.array(coefficient_matrix, dtype=float)
        self.right_hand_side = np.array(right_hand_side, dtype=float)

    @check_square
    @check_singular
    def solve(self):
        """
        Solves the system of linear equations using the matrix inversion method.

        Returns:
        A list representing the solutions to the system of equations.

        Raises:
        ValueError: If the coefficient matrix is singular and cannot be inverted.
        """
        inverse_matrix = np.linalg.inv(self.coefficient_matrix)
        solution = np.dot(inverse_matrix, self.right_hand_side)
        return solution.tolist()