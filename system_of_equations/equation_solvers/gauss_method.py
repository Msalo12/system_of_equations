import numpy as np

from system_of_equations.decorator.decorators import check_square
class GaussMethod:
    """
    A class for performing Gaussian elimination on a matrix to solve linear systems of equations.

    Methods:
    - __init__(self, matrix): Initializes the Gaussian solver with a matrix.
    - upper_triangle_form(self): Reduces the matrix to its upper triangular form.
    - solve_linear_system(self): Solves a system of linear equations represented by the augmented matrix.

    Attributes:
    - matrix: The matrix to be operated on.

    Note:
    - The matrix must be augmented with the right-hand side of the equations to use this solver.
    - The matrix is expected to have one unique solution, and the solver may raise ValueError for inconsistent or singular systems.
    """

    def __init__(self, matrix):
        """
        Initializes the Gaussian solver with a matrix.


        Parameters:
        - matrix: The matrix representing a system of linear equations, including the right-hand side.
        """
        self.matrix = np.array(matrix, dtype=float)

    def upper_triangle_form(self):
        """
        Reduces the matrix to its upper triangular form.

        Raises:
        ValueError if the matrix cannot be reduced to upper triangular form (e.g., inconsistent system).
        """
        n = len(self.matrix)
        for i in range(n):
            # Search for maximum in this column
            max_el = abs(self.matrix[i][i])
            max_row = i
            for k in range(i + 1, n):
                if abs(self.matrix[k][i]) > max_el:
                    max_el = abs(self.matrix[k][i])
                    max_row = k

            # Swap maximum row with current row
            self.matrix[[i, max_row]] = self.matrix[[max_row, i]]

            # Make all rows below this one 0 in current column
            for k in range(i + 1, n):
                c = -self.matrix[k][i] / self.matrix[i][i]
                for j in range(i, n + 1):
                    if i == j:
                        self.matrix[k][j] = 0
                    else:
                        self.matrix[k][j] += c * self.matrix[i][j]

        return self.matrix


    def solve_linear_system(self):
        """
        Solves a system of linear equations represented by the augmented matrix using the Gaussian elimination method.

        Returns:
        A list of solutions to the system of equations or None if there is no unique solution.

        Raises:
        ValueError if the matrix cannot be reduced to upper triangular form (e.g., inconsistent system).
        """

        self.upper_triangle_form()

        n = len(self.matrix)
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = self.matrix[i][n] / self.matrix[i][i]
            for k in range(i - 1, -1, -1):
                self.matrix[k][n] -= self.matrix[k][i] * x[i]

        return x.tolist()
