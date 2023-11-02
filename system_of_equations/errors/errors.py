import numpy as np

class LinearEquationError(Exception):
    """Базовий клас для помилок системи лінійних рівнянь."""
    pass

class NonSquareMatrixError(LinearEquationError):
    """Помилка для випадків, коли матриця не є квадратною."""
    def __init__(self, matrix):
        self.matrix = matrix
        super().__init__(f"Матриця розміру {matrix.shape} не є квадратною!")

    @classmethod
    def check(cls, matrix):
        if matrix.shape[0] != matrix.shape[1]:
            raise cls(matrix)

class SingularMatrixError(LinearEquationError):
    """Помилка для випадків, коли матриця є сингулярною (невизначена або вироджена)."""
    def __init__(self):
        super().__init__("Матриця є сингулярною або виродженою!")

    @classmethod
    def check(cls, matrix):
        if np.linalg.det(matrix) == 0:
            raise cls()

class IterationDivergenceError(LinearEquationError):
    """Помилка, що вказує на розбіжність методу ітерації."""
    def __init__(self, max_iterations):
        super().__init__(f"Метод ітерації розбіжний після {max_iterations} ітерацій!")

class InvalidMatrixStructureError(LinearEquationError):
    """Помилка для випадків, коли матриця не відповідає очікуваній структурі."""
    def __init__(self, matrix, expected_type):
        self.matrix = matrix
        super().__init__(f"Матриця не відповідає очікуваній структурі: {expected_type}")

    @classmethod
    def check_for_tridiagonal(cls, matrix):
        off_diagonal_sum = sum(abs(matrix[i, j]) for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) if abs(i-j) > 1)
        if off_diagonal_sum != 0:
            raise cls(matrix, "трьохдіагональна")

class ConvergenceError(LinearEquationError):
    """Помилка, що вказує на проблеми із збіжністю методу."""
    def __init__(self):
        super().__init__("Проблеми із збіжністю методу!")
