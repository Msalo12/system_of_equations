import numpy as np
class TridiagonalMatrixMethod:

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
        assert len(b) == len(d), "The main diagonal and the free term vector must be of the same length."
        assert len(a) == len(b) - 1, "The sub-diagonal must have one element less than the main diagonal."
        assert len(c) == len(b) - 1, "The super-diagonal must have one element less than the main diagonal."

        self.a = np.array(a, dtype=float)
        self.b = np.array(b, dtype=float)
        self.c = np.array(c, dtype=float)
        self.d = np.array(d, dtype=float)

    def solve_linear_system(self):
        """
        Solves the system of linear equations represented by the tridiagonal matrix.

        Returns:
        A list of solutions for the system of equations or None if there is no unique solution.

        Raises:
        ValueError if the system is inconsistent or singular.
        """
        n = len(self.d)
        # Forward sweep
        for i in range(1, n):
            w = self.a[i - 1] / self.b[i - 1]
            self.b[i] -= w * self.c[i - 1]
            self.d[i] -= w * self.d[i - 1]

        # Back substitution
        x = np.zeros(n)
        x[-1] = self.d[-1] / self.b[-1]
        for i in range(n - 2, -1, -1):
            x[i] = (self.d[i] - self.c[i] * x[i + 1]) / self.b[i]

        return x.tolist()