# Gauss-Jordan Method for Solving Linear Systems of Equations

This Python class performs Gauss-Jordan elimination on a matrix to solve systems of linear equations.

## Initialization
Initialize the Gauss-Jordan solver with a matrix:

```python
from linear_system_solver import GaussJordanMethod
import numpy as np

# Example matrix initialization
matrix = np.array([[2, -1, 1, 8],
                   [3, 2, -1, 1],
                   [1, 3, 4, 9]])

solver = GaussJordanMethod(matrix)
```
## Reduce to Reduced Row-Echelon Form (RREF)
Reduce the matrix to its RREF:

```python
try:
    solver.reduce_to_rref()
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
The matrix must be augmented with the right-hand side of the equations. </br>
The solver may raise ValueError for inconsistent or singular systems.