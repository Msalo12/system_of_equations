import numpy as np
class SimpleIterationMethod:
    """
    A class for solving a system of linear equations using the Simple Iteration Method.

    Methods:
    - __init__(self, matrix, initial_guess, tolerance, max_iterations): Initializes the solver with the necessary parameters.
    - solve(self): Solves the system of linear equations using the Simple Iteration Method.

    Attributes:
    - matrix: The coefficient matrix of the system of linear equations.
    - initial_guess: The initial guess for the solution.
    - tolerance: The tolerance value for convergence.
    - max_iterations: The maximum number of iterations allowed.

    Note:
    - The matrix must be diagonally dominant or strictly diagonally dominant for convergence.
    - The method may not converge for some systems, and it's important to set a reasonable tolerance and maximum iterations.

    """

    def __init__(self, matrix, initial_guess, tolerance, max_iterations):
        """
        Initializes the Simple Iteration Method solver with the necessary parameters.

        Parameters:
        - matrix: The coefficient matrix of the system of linear equations.
        - initial_guess: The initial guess for the solution.
        - tolerance: The tolerance value for convergence.
        - max_iterations: The maximum number of iterations allowed.
        """

        self.matrix = np.array(matrix, dtype=float)
        self.initial_guess = np.array(initial_guess, dtype=float)
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def is_diagonally_dominant(self, mat):
        for i in range(len(mat)):
            sum = 0
            for j in range(len(mat)):
                if i != j:
                    sum += abs(mat[i][j])
            if abs(mat[i][i]) <= sum:
                return False
        return True
    def solve(self):
        """
        Solves the system of linear equations using the Simple Iteration Method.

        Returns:
        A list representing the approximate solution to the system of equations.

        Raises:
        ValueError if the method does not converge within the specified maximum iterations.
        """
        if not self.is_diagonally_dominant(self.matrix):
            raise ValueError("Matrix is not diagonally dominant, method may not converge.")

        x = self.initial_guess
        for _ in range(self.max_iterations):
            x_new = np.copy(x)
            for i in range(len(self.matrix)):
                sum = 0
                for j in range(len(self.matrix)):
                    if i != j:
                        sum += self.matrix[i][j] * x[j]
                x_new[i] = (self.matrix[i][-1] - sum) / self.matrix[i][i]

            if np.linalg.norm(x_new - x) < self.tolerance:
                return x_new.tolist()
            x = x_new

        raise ValueError("Method did not converge within the maximum number of iterations.")
