class Matrix:
    def __init__(self, a, b):
        self.A = a
        self.B = b
        self.num_rows_A, self.num_cols_A = len(self.A), len(self.A[0])
        self.num_rows_B, self.num_cols_B = len(self.B), len(self.B[0])

        self.constraints()

    def constraints(self):
        if self.num_cols_A != self.num_rows_B:
            raise ValueError("The number of columns in A must equal the number of rows in B")

    def naive(self):
        # Ensure the number of columns in A equals the number of rows in B


        # Initialize result matrix C with zeros
        C = [[0 for _ in range(self.num_cols_B)] for _ in range(self.num_rows_A)]

        # Perform matrix multiplication
        for i in range(self.num_rows_A):
            for j in range(self.num_cols_B):
                for k in range(self.num_cols_A):
                    C[i][j] += self.A[i][k] * self.B[k][j]

        return C

    def strassen(self):
        pass

# Create instances of the Matrix class and call the naive method
print(Matrix([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]]).naive())
print(Matrix([[1, 2]], [[1], [2]]).naive())
print(Matrix([[1, 2, 3]], [[1], [2]]).naive())
