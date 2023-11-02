class TridiagonalSolver:
    """
    A class for solving linear systems of equations represented by a tridiagonal matrix.

    Methods:
    - __init__(self, a, b, c, d): Initializes the tridiagonal matrix solver with coefficients a, b, c, and the free terms d.
    - solve_linear_system(self): Solves the system of linear equations represented by the tridiagonal matrix.

    Attributes:
    - a: Diagonal below the main diagonal of the matrix.
    - b: Main diagonal of the matrix.
    - c: Diagonal above the main diagonal of the matrix.
    - d: Vector of free terms.

    Note:
    - The system is expected to have one unique solution, and the solver might raise ValueError for inconsistent systems.
    """

    def __init__(self, a, b, c, d):
        """
        Initializes the tridiagonal matrix solver.

        Parameters:
        - a: Diagonal below the main diagonal of the matrix.
        - b: Main diagonal of the matrix.
        - c: Diagonal above the main diagonal of the matrix.
        - d: Vector of free terms.
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def solve_linear_system(self):
        """
        Solves the system of linear equations represented by the tridiagonal matrix.

        Returns:
        A list of solutions for the system of equations or None if there is no unique solution.

        Raises:
        ValueError if the system is inconsistent or singular.
        """