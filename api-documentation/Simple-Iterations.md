# Simple Iteration Method for Solving Linear Systems of Equations

This Python class provides functionality to solve a system of linear equations using the Simple Iteration Method.

## Initialization
Initialize the solver with the necessary parameters:

```python
import numpy as np
from linear_system_solver import SimpleIterationMethod

# Example initialization
matrix = np.array([[2, -1, 1],
                   [3, 2, -1],
                   [1, 3, 4]])

initial_guess = np.array([0, 0, 0])
tolerance = 0.0001
max_iterations = 100

solver = SimpleIterationMethod(matrix, initial_guess, tolerance, max_iterations)
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
The matrix must be diagonally dominant or strictly diagonally dominant for convergence.</br>
The method may not converge for some systems, and it's important to set a reasonable tolerance and maximum iterations.