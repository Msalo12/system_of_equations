# Tridiagonal Matrix Method for Solving Linear Systems of Equations

This Python class provides functionality to solve linear systems of equations represented by a tridiagonal matrix.


## Initialization

Initialize the solver with the coefficients `a`, `b`, `c`, and the free terms `d`:

```python
import numpy as np
from linear_system_solver import TridiagonalMatrixMethod

# Example initialization
a = np.array([1, 2, 3])  # Diagonal below the main diagonal
b = np.array([4, 5, 6])  # Main diagonal
c = np.array([7, 8, 9])  # Diagonal above the main diagonal
d = np.array([10, 11, 12])  # Vector of free terms

solver = TridiagonalMatrixMethod(a, b, c, d)
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
The system is expected to have one unique solution, and the solver might raise a ValueError for inconsistent systems.