# 코드업 파이썬 기초 100제
# 6096

d = [list(map(int, input().split())) for _ in range(19)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(19) :
        if d[i][y-1] == 0 :
            d[i][y-1] = 1
        else :
            d[i][y-1] = 0

        if d[x-1][i] == 0 :
            d[x-1][i] = 1
        else :
            d[x-1][i] = 0
for j in range(19):
    print(*d[j])