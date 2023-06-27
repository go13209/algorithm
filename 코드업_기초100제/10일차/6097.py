# 코드업 파이썬 기초 100제
# 6097

h, w = map(int, input().split())
graph = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    for i in range(h):
        if d == 0:
            for j in range(y-1, (y-1)+l):
                graph[x-1][j] = 1
        else:
            for k in range(x-1, (x-1)+l):
                graph[k][y-1] = 1
for m in range(h):
    print(*graph[m])