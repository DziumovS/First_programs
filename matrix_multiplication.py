n, m = (int(i) for i in input().split())
matrix_1 = [[int(i) for i in input().split()] for x in range(n)]
input()
m, k = (int(i) for i in input().split())
matrix_2 = [[int(i) for i in input().split()] for z in range(m)]
matrix_3= [[0 for _ in range(n)] for _ in range(k)]

for i in range(n):
    for j in range(k):
        temp = 0
        for l in range(m):
            temp += matrix_1[j][l] * matrix_2[l][i]
        matrix_3[j][i] += temp

for i in range(n):
    for j in range(k):
        print(str(matrix_3[i][j]).ljust(4), end='')
    print()