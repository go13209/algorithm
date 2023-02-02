T = int(input())

for _ in range(T):
    n = int(input()) # 0 1
    m = int(input()) # 0 1 2
    matrix = [[0] * m for _ in range(n + 1)]
    
    for i in range(m):
        matrix[0][i] = i + 1
    
    for j in range(1, n+1):
        for k in range(m):
            matrix[j][k] = sum(matrix[j-1][:k+1])
    print(matrix[n][m-1])