# Matrix Method for Solving Linear Systems of Equations

This Python class provides functionality to solve a system of linear equations using the matrix inversion method.

## Initialization
Initialize the solver with the coefficient matrix and right-hand side vector:

```python
import numpy as np
from system_of_equations.decorator.decorators import check_square, check_singular
from linear_system_solver import MatrixMethod

# Example matrix initialization
coefficient_matrix = np.array([[2, -1, 1],
                               [3, 2, -1],
                               [1, 3, 4]])

right_hand_side = np.array([8, 1, 9])

solver = MatrixMethod(coefficient_matrix, right_hand_side)
```
## Solve Linear System of Equations
Solve the system of linear equations:

```python
try:
    solutions = solver.solve()
    print("Solution:", solutions)
except ValueError as e:
    print(f"Error: {e}")
```

## Notes
The coefficient matrix must be square and non-singular for the matrix inversion method to work.<br>
The method raises a ValueError if the coefficient matrix is singular and cannot be inverted.