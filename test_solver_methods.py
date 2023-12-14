from system_of_equations.equation_solvers.gauss_jordan_method import GaussJordanMethod
from system_of_equations.equation_solvers.gauss_method import GaussMethod
from system_of_equations.equation_solvers.matrix_method import MatrixMethod
from system_of_equations.equation_solvers.simple_iterations_method import SimpleIterationMethod
from system_of_equations.equation_solvers.three_diagonal_matrix_method import TridiagonalMatrixMethod
from system_of_equations.equation_solvers.linear_equation_solver import LinearEquationSolver

# Test for GaussJordanMethod
print("Testing GaussJordanMethod...")
matrix = [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
gj_method = GaussJordanMethod(matrix)
print("Solution:",  [round(x, 2) for x in gj_method.solve_linear_system()])

# Test for GaussMethod

print("\nTesting GaussMethod...")
matrix = [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
gm_method = GaussMethod(matrix)
print("Solution:",  [round(x, 2) for x in gm_method.solve_linear_system()])

# Test for MatrixMethod
print("\nTesting MatrixMethod...")
coefficient_matrix = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
right_hand_side = [1, 2, 3]
mm_method = MatrixMethod(coefficient_matrix, right_hand_side)
print("Solution:",  [round(x, 2) for x in mm_method.solve_linear_system()])

# Test for SimpleIterationMethod
print("\nTesting SimpleIterationMethod...")
matrix = [[4, 1, 1], [2, 5, 1], [1, 2, 4]]
initial_guess = [1, 1, 1]
tolerance = 0.01
max_iterations = 100
si_method = SimpleIterationMethod(matrix, initial_guess, tolerance, max_iterations)
print("Solution:",  [round(x, 2) for x in si_method.solve_linear_system()])

# Test for TridiagonalMatrixMethod
print("\nTesting TridiagonalMatrixMethod...")
# Example tridiagonal matrix components
a = [1, 1]  # Below main diagonal (2 elements)
b = [4, 4, 4]  # Main diagonal (3 elements)
c = [1, 1]  # Above main diagonal (2 elements)
d = [7, 8, 5]  # Right-hand side (3 elements)
 # Free terms
td_method = TridiagonalMatrixMethod(a, b, c, d)
print("Solution:",  [round(x, 2) for x in td_method.solve_linear_system()])
