# 코드업 파이썬 기초 100제
# 6098

graph = [list(map(int, input().split())) for _ in range(10)]
x, y = (1, 1)
graph[x][y] = 9
while True:
    if y + 1 < 9 and graph[x][y+1] == 0 or graph[x][y+1] == 2:
        x, y = (x, y+1)
        if graph[x][y] == 2:
            graph[x][y] = 9
            break
        else:
            graph[x][y] = 9
    elif x + 1 < 9 and graph[x][y+1] == 1:
        x, y = (x+1, y)
        if graph[x][y] == 2:
            graph[x][y] = 9
            break
        else:
            graph[x][y] = 9
    else:
        break

for i in range(10):
    print(*graph[i])