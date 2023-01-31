T = int(input())
for _ in range(T):
    m, n = map(int, input().split())

    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))

    new_matrix = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            new_matrix[i][j] = matrix[m-j-1][i]

    cnt = 0
    for a in new_matrix:
        for b in range(len(a)):
            if a[b] == 0:
                try:
                    if a.index(1, b) >= 0:
                        first_1 = a.index(1, b)
                        cnt += first_1 - b
                        a[b], a[first_1] = a[first_1], a[b]
                except:
                    continue
    print(cnt)