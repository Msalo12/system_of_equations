class Matrix:
    """
    A class representing a mathematical matrix.

    Attributes:
    - rows: The number of rows in the matrix.
    - columns: The number of columns in the matrix.
    - data: A two-dimensional list storing the matrix elements.

    Methods:
    - __init__(self, rows, columns, data=None): Initializes a matrix with the specified dimensions.
    - __str__(self): Returns a string representation of the matrix.
    - __add__(self, other): Performs matrix addition with another matrix of the same dimensions.
    - __sub__(self, other): Performs matrix subtraction with another matrix of the same dimensions.
    - __mul__(self, other): Performs matrix multiplication with another matrix that satisfies the multiplication rule.
    - transpose(self): Returns the transpose of the matrix, swapping rows and columns.

    Note:
    - Matrix dimensions must match for addition and subtraction.
    - For multiplication, the number of columns in the first matrix must match the number of rows in the second matrix.
    - Other matrix operations can be added as needed.
    """

    def __init__(self, rows, columns, data=None):
        self.rows = rows
        self.columns = columns
        if data is None:
            # Initialize the matrix with zeros
            self.data = [[0 for _ in range(columns)] for _ in range(rows)]
        else:
            # Initialize the matrix with the provided data
            if len(data) != rows or any(len(row) != columns for row in data):
                raise ValueError("Invalid matrix dimensions")
            self.data = data

    def __str__(self):
        """
        Returns a string representation of the matrix.

        Example:
        1  2  3
        4  5  6
        7  8  9
        """
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        """
        Performs matrix addition with another matrix of the same dimensions.

        Parameters:
        - other: Another matrix to add to this matrix.

        Returns:
        A new matrix representing the sum of the two matrices.

        Raises:
        ValueError if matrix dimensions do not match.
        """
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for addition")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(self.rows, self.columns, result)

    def __sub__(self, other):
        """
        Performs matrix subtraction with another matrix of the same dimensions.

        Parameters:
        - other: Another matrix to subtract from this matrix.

        Returns:
        A new matrix representing the result of the subtraction.

        Raises:
        ValueError if matrix dimensions do not match.
        """

        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for subtraction")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(self.rows, self.columns, result)

    def __mul__(self, other):
        """
        Performs matrix multiplication with another matrix that satisfies the multiplication rule.

        Parameters:
        - other: Another matrix to multiply with this matrix.

        Returns:
        A new matrix representing the result of matrix multiplication.

        Raises:
        ValueError if matrix dimensions do not match for multiplication.
        """
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.columns)) for j in range(other.columns)] for i in range(self.rows)]
        return Matrix(self.rows, other.columns, result)

    def transpose(self):
        """
        Returns the transpose of the matrix, swapping rows and columns.

        Returns:
        A new matrix representing the transpose of the original matrix.
        """
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(self.columns, self.rows, result)

    # Other matrix operations can be added here as needed
