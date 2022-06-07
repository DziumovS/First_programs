n, m = (int(i) for i in input().split())
matrix = [[0] * m for _ in range(n)]
row, col = 0, 0

for i in range(1, n*m + 1):
    matrix[row][col] = i

    if (col == 0 or matrix[row][col - 1] != 0) and row > 0 and matrix[row - 1][col] == 0:
        row -= 1

    elif 0 <= col + 1 < m and matrix[row][col + 1] == 0:
        col += 1

    elif 0 <= row + 1 < n and matrix[row + 1][col] == 0:
        row += 1

    elif 0 <= col - 1 < m and matrix[row][col - 1] == 0:
        col -= 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()