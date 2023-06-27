# 코드업 파이썬 기초 100제
# 6095

d = [[0 for _ in range(19)] for _ in range(19)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    d[x-1][y-1] = 1
for i in range(19):
    print(*d[i])