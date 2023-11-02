class GaussJordanMethod:
    """
    A class for performing Gauss-Jordan elimination on a matrix to solve linear systems of equations.

    Methods:
    - __init__(self, matrix): Initializes the Gauss-Jordan solver with a matrix.
    - reduce_to_rref(self): Reduces the matrix to its reduced row-echelon form (RREF).
    - solve_linear_system(self): Solves a system of linear equations represented by the augmented matrix.
    
    Attributes:
    - matrix: The matrix to be operated on.

    Note:
    - The matrix must be augmented with the right-hand side of the equations to use this solver.
    - The matrix is expected to have one unique solution, and the solver may raise ValueError for inconsistent or singular systems.
    """

    def __init__(self, matrix):
        """
        Initializes the Gauss-Jordan solver with a matrix.

        Parameters:
        - matrix: The matrix representing a system of linear equations, including the right-hand side.
        """

    def reduce_to_rref(self):
        """
        Reduces the matrix to its reduced row-echelon form (RREF).

        Raises:
        ValueError if the matrix cannot be reduced to RREF (e.g., inconsistent system).
        """

    def solve_linear_system(self):
        """
        Solves a system of linear equations represented by the augmented matrix using the Gauss-Jordan elimination method.

        Returns:
        A list of solutions to the system of equations or None if there is no unique solution.

        Raises:
        ValueError if the matrix cannot be reduced to RREF (e.g., inconsistent system).
        """