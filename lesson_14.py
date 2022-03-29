n = int(input())
m = int(input())

matrix = []

c = 0

for i in range(n):
    row = []
    
    for j in range(m):
        row.append(0)
    
    matrix.append(row)

print(matrix)


