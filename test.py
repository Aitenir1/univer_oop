matrix = [
    [2 for i in range(12)],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2 for i in range(12)],

]

c = 3

def explore(i, j, c):
    difs = [-1, 0, 1]
    print(i, j)
    for di in difs:
        for dj in difs:
            print(di, dj, matrix[i+di][j+dj])
            if matrix[i+di][j+dj] == 1 and (di != 0 or dj != 0):
                matrix[i+di][j+dj] = c
                explore(i+di, j+dj, c)

for i in range(1, 12):
    for j in range(1, 12):
        if matrix[i][j] == 1:
            matrix[i][j] = c
            explore(i, j, c)
            c += 1

for i in matrix:
    print(i)