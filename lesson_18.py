class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.r = len(matrix)
        self.c = len(matrix[0])

    def __sub__(self, other):

        n = self.r
        m = self.c

        res_mat = []

        for i in range(n):
            row = []
            for j in range(m):
                row.append(self.matrix[i][j] - other.matrix[i][j])

            res_mat.append(row)

        return Matrix(res_mat)

    def __add__(self, other):
        n = self.r
        m = self.c

        res_mat = []

        for i in range(n):
            row = []
            for j in range(m):
                row.append(self.matrix[i][j] + other.matrix[i][j])

            res_mat.append(row)

        return Matrix(res_mat)

    def __str__(self):
        res = []

        for i in self.matrix:
            res.append(' '.join(map(str, i)))

        return '\n'.join(res)


a = Matrix([
    [1, 2, 3],
    [2, 1, 3],
    [1, 1, 1]
])

b = Matrix([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

s = a + b
d = a - b

print(s)
print()
print(d)
