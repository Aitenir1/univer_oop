class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    @classmethod
    def validate_matrix(cls, matrix):
        first_row = len(matrix[0])
        for row in matrix:
            if len(row) != first_row:
                raise Exception('Your input matrix is not correct!')

    @classmethod
    def determinant_with_no_row_and_col(cls, matrix, x, y):
        # Возвращает определитель матрицы без элементов на строке x и на столбце y
        # Returns a determinant of matrix with no elements on row x and column y

        two_by_two_matrix = []
        for a in range(3):
            for b in range(3):
                if a != x and b != y:
                    two_by_two_matrix.append(matrix[a][b])

        a11 = two_by_two_matrix[0]
        a12 = two_by_two_matrix[1]
        a21 = two_by_two_matrix[2]
        a22 = two_by_two_matrix[3]

        # print(two_by_two_matrix)
        determinant = a11 * a22 - a12 * a21
        # print(two_by_two_matrix)
        # print(determinant)
        return determinant

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, new_matrix):
        self.validate_matrix(new_matrix)
        self.__matrix = new_matrix

    def swap_rows(self, n, m):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        n, m = n - 1, m - 1
        res = []

        for i in range(rows):
            row = []
            if i == n:
                i = m
            elif i == m:
                i = n
            for j in range(cols):
                row.append(self.matrix[i][j])
            res.append(row)

        return res

    def swap_columns(self, n, m):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        n, m = n - 1, m - 1
        res = []

        for i in range(rows):
            row = []
            for j in range(cols):
                if j == n:
                    j = m
                elif j == m:
                    j = n
                row.append(self.matrix[i][j])
            res.append(row)

        return res

    def sum_rows(self):
        result = []
        for i in self.matrix:
            result.append(sum(i))
        return result

    def sum_cols(self):
        res = [0] * len(self.matrix[0])

        rows = len(self.matrix)
        cols = len(res)

        for i in range(rows):
            for j in range(cols):
                res[j] += self.matrix[i][j]

        return res

    def sum_diagonals(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        res = [0, 0]

        for i in range(rows):
            for j in range(cols):
                if i == j:
                    res[0] += self.matrix[i][j]
                if i == cols - j - 1:

                    res[1] += self.matrix[i][j]
        return res

    def transpose(self):
        num_rows = len(self.matrix)
        num_cols = len(self.matrix[0])

        res = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

        for i in range(num_rows):
            for j in range(num_cols):
                res[j][i] = self.matrix[i][j]

        return res

    def adj(self):
        if len(self.matrix) != 3 or len(self.matrix[0]) != 3:
            raise Exception('Мен 3х3 матрицалар үчүн эле иштейм :)')

        res = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for i in range(3):
            for j in range(3):

                determ = self.determinant_with_no_row_and_col(self.matrix, i, j)

                res[i][j] = (-1) ** (i + j) * determ

        return Matrix(res).transpose()

    def determinant(self):
        res = 0

        for i in range(3):
            determinant_two_by_two = self.determinant_with_no_row_and_col(self.matrix, i, 0)

            res += self.matrix[i][0] * determinant_two_by_two * (-1) ** i

        return res

    def inverse(self):
        determ = self.determinant()
        adj = self.adj()

        res = adj.copy()

        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = (1 / determ) * adj[i][j]

        return res


v = [
    [1, -2, 3],
    [0, 4, -1],
    [5, 0, 0],
]

m1 = Matrix(v)

swapped_row = m1.swap_rows(1, 2)
swapped_column = m1.swap_columns(1, 2)

print('INITIAL MATRIX:')
for k in m1.matrix:
    print(k)

print('SWAPPED 1-ROW WITH 2-ROW:')
for k in swapped_row:
    print(k)

print('SWAPPED 1-COLUMN WITH 2-COLUMN:')
for k in swapped_column:
    print(k)

print('SUM OF THE ROWS:')
print(m1.sum_rows())
print('SUM OF THE COLUMNS:')
print(m1.sum_cols())
print('SUM OF THE DIAGONAL:')
print(m1.sum_diagonals())


transpose_of_matrix = m1.transpose()
print('TRANSPOSE OF THE MATRIX:')
for k in transpose_of_matrix:
    print(k)

adj_of_matrix = m1.adj()
print('ADJOINT:')
for k in adj_of_matrix:
    print(k)

determinant = m1.determinant()
print('DETERMINANT OF THE MATRIX:')
print(determinant)

inv = m1.inverse()
print('INVERSE OF THE MATRIX:')
for k in inv:
    print(k)