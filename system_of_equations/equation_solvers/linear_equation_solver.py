from abc import ABC, abstractmethod

class LinearEquationSolver(ABC):
    """
    An interface for solving linear equations.
    """

    @abstractmethod
    def solve_linear_system(self):
        """
        Solves a system of linear equations.
        """
        pass
