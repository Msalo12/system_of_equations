class Matrix:
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
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for addition")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(self.rows, self.columns, result)

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for subtraction")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(self.rows, self.columns, result)

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.columns)) for j in range(other.columns)] for i in range(self.rows)]
        return Matrix(self.rows, other.columns, result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(self.columns, self.rows, result)

    # Other matrix operations can be added here as needed
