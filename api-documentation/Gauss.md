# Gaussian Method for Solving Linear Systems of Equations

This Python class performs Gaussian elimination on a matrix to solve systems of linear equations.

## Initialization
Initialize the Gaussian solver with a matrix:

```python

import numpy as np
from system_of_equations.decorator.decorators import check_square
from linear_system_solver import GaussMethod

# Example matrix initialization
matrix = np.array([[2, -1, 1, 8],
                   [3, 2, -1, 1],
                   [1, 3, 4, 9]])

solver = GaussMethod(matrix)
```
## Reduce to Upper Triangular Form
Reduce the matrix to its upper triangular form:

```python
try:
    solver.upper_triangle_form()
    print(solver.matrix)
except ValueError as e:
    print(f"Error: {e}")
```

## Solve Linear System of Equations
Solve the system of linear equations:

```python
try:
    solutions = solver.solve_linear_system()
    print("Solution:", solutions)
except ValueError as e:
    print(f"Error: {e}")
 ```   
## Notes
The matrix must be augmented with the right-hand side of the equations.</br>
The solver may raise ValueError for inconsistent or singular systems.