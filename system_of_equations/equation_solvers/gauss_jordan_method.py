import numpy as np
from system_of_equations.decorator.decorators import check_square, check_singular
from system_of_equations.equation_solvers.linear_equation_solver import LinearEquationSolver


class GaussJordanMethod(LinearEquationSolver):

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
        self.matrix = np.array(matrix, dtype=float)
    #@check_square
    def reduce_to_rref(self):
        """
        Reduces the matrix to its reduced row-echelon form (RREF).

        Raises:
        ValueError if the matrix cannot be reduced to RREF (e.g., inconsistent system).
        """
        m, n = self.matrix.shape
        for i in range(m):
            if self.matrix[i, i] == 0:
                raise ValueError("Matrix cannot be reduced to RREF (singular matrix).")
            self.matrix[i] = self.matrix[i] / self.matrix[i, i]
            for j in range(m):
                if i != j:
                    self.matrix[j] = self.matrix[j] - self.matrix[i] * self.matrix[j, i]
        return self.matrix


    @check_singular
    def solve_linear_system(self):
        """
        Solves a system of linear equations represented by the augmented matrix using the Gauss-Jordan elimination method.

        Returns:
        A list of solutions to the system of equations or None if there is no unique solution.

        Raises:
        ValueError if the matrix cannot be reduced to RREF (e.g., inconsistent system).
        """
        self.reduce_to_rref()
        # Assuming the last column is the solution column after RREF
        solutions = self.matrix[:, -1]
        return solutions.tolist()