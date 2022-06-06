n, s, k, matrix, q, n0, n1 = input(), [8, 7, 6, 5, 4, 3, 2, 1], ['a', 'b', 'c', 'd', 'e', 'f', 'g','h'], [], [], 0, 0

for i in s:
    for j in k:
        temp = [j + str(i)]
        q += temp
    matrix.append(q)
    q = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == n:
            matrix[i][j], n0, n1 = 'N', i, j

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i == n0 + 2 or i == n0 -2) and (j == n1 + 1 or j == n1 - 1):
            matrix[i][j] = '*'
        if (i == n0 + 1 or i == n0 - 1) and (j == n1 + 2 or j == n1 - 2):
            matrix[i][j] = '*'
        if matrix[i][j] != 'N' and matrix[i][j] != '*':
            matrix[i][j] = '.'

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=' ')
    print()